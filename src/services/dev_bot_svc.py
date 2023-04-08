import random

from constants import MIN_COMMITS, MAX_COMMITS
from services.git_svc import GitService
from services.jira_svc import JiraService


class DevBotService:
    def __init__(self):
        self._jira_bot = JiraService()
        self._git_bot = GitService()

    def run(self, task: str):
        match task:
            case "dev":
                self._dev_run()
            case "merge":
                self._merge_run()

    def _dev_run(self):
        number_of_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
        tickets_created_list = self._jira_bot.create_jira_tickets()
        self._git_bot.produce_pull_request(number_of_commits, tickets_created_list)

    def _merge_run(self):
        self._git_bot._merge_prs()
