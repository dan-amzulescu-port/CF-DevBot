import os
import random
import requests
import json

from typing import List
from git import Repo

from blob_constants import BUSLOG_COMMIT_MSGS, CTRLR_COMMIT_MSGS, FLASKUI_COMMIT_MSGS, PYTHON_COMMANDS, \
    BRANCHES_NAMES_PREFIXES, BRANCHES_NAMES, PULL_REQUESTS_TITLES
from constants import GIT_USER, GIT_PAT, APERTURE_ORG, APERTURE_REPO_SHORT, APERTURE_REPO_URL, GIT_USERS, \
    TRIO_SERVICES_LIST, GH_API_BASE_URL


class GitService:
    def __init__(self, git_user: str = GIT_USER, pat: str = GIT_PAT):
        self._git_user = git_user
        self._pat = pat
        self._repo_name = APERTURE_REPO_SHORT
        self._repo_url_short = APERTURE_REPO_URL
        self._original_dir = os.getcwd()
        self._repo = None
        self._original_head = None

    def produce_pull_request(self, number_of_commits: int, jira_tickets: List[str]):
        self._clone_repo()
        self._create_branch()
        for i in range(0, len(jira_tickets)):
            self._create_commit(jira_tickets[i])
            for j in range(0, number_of_commits):
                self._create_commit()

        self._create_pull_request(
            f"{random.choice(PULL_REQUESTS_TITLES)}",  # title
            f"General fixes/changes + taking care of the following tickets: {' '.join(jira_tickets)}",
            self._repo.head.reference.name,  # head_branch
            "main",  # base_branch
            os.environ['GIT_PASSWORD'],  # git_token
        )

    def _clone_repo(self):
        os.chdir(self._original_dir)
        os.mkdir("repo")
        os.chdir(self._original_dir + os.sep + "repo")

        remote = f"https://{self._repo_url_short}"
        self._repo = Repo.clone_from(remote, os.getcwd())

    def _create_branch(self):
        new_branch_name = f"{random.choice(BRANCHES_NAMES_PREFIXES)}{random.choice(BRANCHES_NAMES)}"
        os.environ['GIT_USERNAME'] = self._git_user
        os.environ['GIT_PASSWORD'] = self._pat
        current = self._repo.create_head(new_branch_name)
        current.checkout()
        self._repo.git.push('--set-upstream', 'origin', self._repo.head)

    def _create_commit(self, jira_ticket_ref: str = ""):
        git_user = random.choice(GIT_USERS)
        os.environ['GIT_USERNAME'] = git_user['git_username']
        os.environ['GIT_PASSWORD'] = git_user['git_pat']
        trio_service = random.choice(TRIO_SERVICES_LIST)
        try:
            self._create_code_change(trio_service)
            commit_msg = GitService._create_commit_msg(jira_ticket_ref, trio_service)
            self._repo.git.add(A=True)
            self._repo.git.commit(m=commit_msg)
            self._repo.git.push('--set-upstream', 'origin', self._repo.head)

        except Exception as e:
            print(e)

    def _create_code_change(self, trio_service):
        with open(self._original_dir + os.sep + "repo" + os.sep + trio_service + os.sep + 'changes.py', 'a') as file:
            file.write(f'{random.choice(PYTHON_COMMANDS)}\n')
        file.close()

    @staticmethod
    def _create_commit_msg(jira_ticket_ref, trio_service):
        match trio_service:
            case "buslog":
                commit_msg = random.choice(BUSLOG_COMMIT_MSGS) + " - " + jira_ticket_ref
            case "ctrlr":
                commit_msg = random.choice(CTRLR_COMMIT_MSGS) + " - " + jira_ticket_ref
            case "flask-ui":
                commit_msg = random.choice(FLASKUI_COMMIT_MSGS) + " - " + jira_ticket_ref
            case _:
                commit_msg = "!"
        return commit_msg

    @staticmethod
    def _create_pull_request(title, description, source_branch, target_branch, git_token):
        """Creates the pull request for the head_branch against the base_branch"""

        git_pulls_api = f"{GH_API_BASE_URL}/repos/{APERTURE_ORG}/{APERTURE_REPO_SHORT}/pulls"
        headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"Bearer {git_token}"}
        payload = GitService._create_pr_payload(description, source_branch, target_branch, title)
        r = requests.post(git_pulls_api, headers=headers, data=json.dumps(payload))

        if not r.ok:
            print("Request Failed: {0}".format(r.text))

    @staticmethod
    def _create_pr_payload(description, source_branch, target_branch, title):
        payload = {
            "title": title,
            "body": description,
            "head": f"{APERTURE_ORG}:{source_branch}",
            "base": f"{target_branch}",
        }
        return payload

    def _merge_prs(self):
        git_token = self._pat
        pulls_url = f"{GH_API_BASE_URL}/repos/{APERTURE_ORG}/{APERTURE_REPO_SHORT}/pulls?state=open"
        headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"Bearer {git_token}"}
        response = requests.get(pulls_url, headers=headers)
        pulls = response.json()

        if len(pulls) > 4:
            # Loop through the first 3 pull requests and leave them unmerged
            for i in range(3):
                print(f"Pull Request #{pulls[i]['number']} - '{pulls[i]['title']}' will be left unmerged.")

            # Loop through the remaining pull requests and merge them
            for i in range(3, len(pulls)):
                GitService._merge_pull_request(pulls[i], git_token)
        elif len(pulls) > 0:
            GitService._merge_pull_request(pulls[0], git_token)
        else:
            print("There are no open pull requests to merge.")

    @staticmethod
    def _merge_pull_request(pull, git_token):
        headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"Bearer {git_token}"}
        pull_number = pull["number"]
        merge_url = f"{GH_API_BASE_URL}/repos/{APERTURE_ORG}/{APERTURE_REPO_SHORT}/pulls/{pull_number}/merge"
        response = requests.put(merge_url, headers=headers)

        if response.status_code == 200:
            print(f"Pull Request #{pull_number} merged successfully.")
        else:
            print(f"Failed to merge Pull Request #{pull_number}. Status code: {response.status_code}")
