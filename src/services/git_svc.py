import os
import random
import requests
import subprocess
import logging

from typing import Dict, List

from blob_constants import (
    SERVICE1_COMMIT_MSGS,
    SERVICE2_COMMIT_MSGS,
    SERVICE3_COMMIT_MSGS,
    PYTHON_COMMANDS,
    BRANCHES_NAMES_PREFIXES,
    BRANCHES_NAMES,
    PULL_REQUESTS_TITLES,
    SERVICE_COMMIT_MSGS,
)
from helpers.git_functions import validate_git_config_is_set, get_github_headers, get_default_branch
from helpers.logging_functions import handle_error, handle_success, handle_subprocess_output
from model.git_data import GitData
from services.data_var_svc import get_random_app_service_name_and_id

logging.basicConfig(level=logging.INFO)  # Set logging level to DEBUG
logger = logging.getLogger(__name__)  # Create a logger for the current module


class GitService:
    def __init__(self):
        validate_git_config_is_set()
        self._git_data = GitData()
        self._username = ""
        self._password = ""
        self._set_gituser_cred()
        self._original_dir = os.getcwd()
        # self._repo = Repo()
        self._original_head = None

    def _set_gituser_cred(self) -> None:
        main_git_user_id = str(random.randint(1, self._git_data.git_users_count))
        self._username = os.environ[f"GIT_USER{main_git_user_id}"]
        self._password = os.environ[f"GIT_PAT{main_git_user_id}"]
        subprocess.run(['git', 'config', '--global', 'user.name', self._username])
        subprocess.run(['git', 'config', '--global', 'user.password', self._password])

    def produce_pull_request(self, jira_tickets: List[str]) -> None:
        number_of_commits = random.randint(int(os.environ['MIN_COMMITS']), int(os.environ['MAX_COMMITS']))
        self._clone_repo()
        new_branch_name = self._create_branch()
        app_service, app_service_id = get_random_app_service_name_and_id()
        for i in range(0, len(jira_tickets)):
            self._create_commit(app_service, app_service_id, jira_tickets[i])
            for j in range(0, number_of_commits):
                self._create_commit(app_service, app_service_id)

        self._create_pull_request(
            f"{random.choice(PULL_REQUESTS_TITLES)}",  # title
            f"General fixes/changes + taking care of the following tickets: {' '.join(jira_tickets)}",
            get_default_branch(url=f"https://{self._git_data.repo_url_short}", token=self._password),
            new_branch_name  # base
        )

    def _clone_repo(self) -> None:
        self._cd_to_repo_dir()

        clone_command = f'git clone https://{self._username}:{self._password}@{self._git_data.repo_url_short}.git .'
        result = subprocess.run(clone_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            handle_success(f'Repository {self._git_data.repo_url_short} cloned successfully.')
        else:
            handle_error(f'Failed to clone repository. Error: {result.stderr.decode("utf-8")}')

    def _cd_to_repo_dir(self) -> None:
        os.chdir(self._original_dir)
        os.mkdir("repo")
        os.chdir(f"{self._original_dir}{os.sep}repo")

    def _create_branch(self) -> str:
        new_branch_name = f"{random.choice(BRANCHES_NAMES_PREFIXES)}{random.choice(BRANCHES_NAMES)}"

        GitService._create_local_branch(new_branch_name)
        self._git_push(new_branch_name)
        return new_branch_name

    def _git_push(self, branch: str) -> None:
        command = f"git push https://{self._username}:{self._password}@{self._git_data.repo_url_short}.git {branch}"
        push_result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        handle_subprocess_output(push_result, "<Pushing Git Changes>")

    @staticmethod
    def _create_local_branch(new_branch_name: str) -> None:
        create_branch_result = subprocess.run(['git', 'checkout', '-b', new_branch_name])
        handle_subprocess_output(create_branch_result, "<Creating local Git Branch>")

    def _create_commit(self, app_service: str, app_service_id: int, jira_ticket_ref: str = "", ) -> None:
        self._set_gituser_cred()

        try:
            self._create_code_change(app_service)
            commit_msg = GitService.create_commit_msg(jira_ticket_ref, app_service_id)
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', commit_msg])
            result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE, text=True)
            current_branch = result.stdout.strip()
            self._git_push(current_branch)

        except Exception as e:
            print(e)

    def _create_code_change(self, app_service: str) -> None:
        app_folder = ""
        if app_service:
            app_folder = f"{os.sep}{app_service}"

        with open(f"{self._original_dir}{os.sep}repo{app_folder}{os.sep}changes.py", 'a') as file:
            file.write(f'{random.choice(PYTHON_COMMANDS)}\n')

    @staticmethod
    def create_commit_msg(jira_ticket_ref, app_service_id) -> str:
        postfix = ""
        if jira_ticket_ref:
            postfix += f"' - '{jira_ticket_ref}"
        match app_service_id:
            case 1:
                commit_msg = f"{random.choice(SERVICE1_COMMIT_MSGS)}{postfix}"
            case 2:
                commit_msg = f"{random.choice(SERVICE2_COMMIT_MSGS)}{postfix}"
            case 3:
                commit_msg = f"{random.choice(SERVICE3_COMMIT_MSGS)}{postfix}"
            case _:
                commit_msg = f"{random.choice(SERVICE_COMMIT_MSGS)}{postfix}"
        return commit_msg

    def _create_pull_request(self, title, description, source_branch, target_branch):
        """Creates the pull request for the head_branch against the base_branch"""
        headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"Bearer {self._password}"}
        payload = {
            "title": title,
            "body": description,
            "head": f"{self._git_data.repo_org}:{target_branch}",
            "base": f"{source_branch}",
        }
        r = requests.post(self._git_data.git_pulls_api, headers=headers, json=payload)

        if not r.ok:
            print("Request Failed: {0}".format(r.text))

    def _create_pr_payload(self, description, source_branch, target_branch, title) -> Dict[str, str]:
        payload = {
            "title": title,
            "body": description,
            "head": f"{self._git_data.repo_org}:{source_branch}",
            "base": f"{target_branch}",
        }
        return payload

    def merge_prs(self):
        git_token = self._password
        pulls = self.get_pull_requests(git_token)

        if len(pulls) > 4:
            # Loop through the first 3 pull requests and leave them unmerged
            for i in range(3):
                print(f"Pull Request #{pulls[i]['number']} - '{pulls[i]['title']}' will be left unmerged.")
            # Loop through the remaining pull requests and merge them
            for i in range(3, len(pulls)):
                self._merge_pull_request(pulls[i], git_token)
        elif len(pulls) > 0:
            self._merge_pull_request(pulls[0], git_token)
        else:
            print("There are no open pull requests to merge.")

    def get_pull_requests(self, git_token: str):
        pulls_url = f"{self._git_data.git_pulls_api}?state=open"
        response = requests.get(pulls_url, headers=get_github_headers(git_token))
        pulls = response.json()
        return pulls

    def _merge_pull_request(self, pull, git_token):
        pull_num = pull["number"]
        merge_url = f"{self._git_data.git_pulls_api}/{pull_num}/merge"
        response = requests.put(merge_url, headers=get_github_headers(git_token))

        if response.status_code == 200:
            print(f"Pull Request #{pull_num} merged successfully.")
        else:
            print(f"Failed to merge Pull Request #{pull_num}. Status code: {response.status_code}")
