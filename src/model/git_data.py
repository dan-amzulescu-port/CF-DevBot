import os

from constants import GH_API_BASE_URL


class GitData:
    def __init__(self):
        self.git_users_count = int(os.getenv('GIT_USERS_COUNT'))
        self.repo_git_server = os.getenv('REPO_GIT_SERVER')
        self.repo_org = os.getenv('REPO_ORG')
        self.repo_name = os.getenv('REPO_NAME')
        self.repo_url_short = f"{self.repo_git_server}/{self.repo_org}/{self.repo_name}"
        self.git_pulls_api = f"{GH_API_BASE_URL}/repos/{self.repo_org}/{self.repo_name }/pulls"
