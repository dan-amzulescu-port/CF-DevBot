from services.data_var_svc import DataVarService
from services.git_svc import GitService
from services.jira_svc import JiraService


class DevBotService:
    def __init__(self):
        self._data_service = DataVarService()
        self._git_bot = GitService()

    def run(self, task: str):
        match task:
            case "dev":
                self._dev_run()
            case "merge_prs":
                self._merge_run()
            case "close_prs":
                self._close_run()
            case "clean_changes":
                self._clean_changes_run()
            case _:
                raise ValueError('Invalid option was set (only "dev" and "merge" currently supported): ' + task)

    def _dev_run(self):
        jira_bot = JiraService()
        tickets_created_list = jira_bot.create_jira_tickets()
        self._git_bot.produce_pull_request(tickets_created_list)

    def _merge_run(self):
        self._git_bot.merge_prs()

    def _close_run(self):
        self._git_bot.close_prs()

    def _clean_changes_run(self):
        self._git_bot.clean_changes()
