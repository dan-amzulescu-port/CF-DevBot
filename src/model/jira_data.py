import os


class JiraData:
    def __init__(self):
        self.project = os.getenv('JIRA_PROJECT')
        self.jira_user_email = os.getenv('JIRA_USER_EMAIL')
        self.jira_token = os.getenv('JIRA_TOKEN')
        self.jira_server = os.getenv('JIRA_SERVER')
        self.min_jira_tickets = int(os.getenv('MIN_JIRA_TICKETS'))
        self.max_jira_tickets = int(os.getenv('MAX_JIRA_TICKETS'))
