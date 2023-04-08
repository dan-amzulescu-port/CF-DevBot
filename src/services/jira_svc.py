import random
from typing import List

from jira import JIRA

from blob_constants import JIRA_TICKETS
from constants import JIRA_USER_EMAIL, JIRA_SERVER, JIRA_PROJECT, JIRA_TOKEN, MIN_JIRA_TICKETS, MAX_JIRA_TICKETS


class JiraService:
    def __init__(self):
        self._project = JIRA_PROJECT
        try:
            self._connection = JIRA(basic_auth=(JIRA_USER_EMAIL, JIRA_TOKEN), server=JIRA_SERVER)
        except Exception as e:
            print(e)

    def create_jira_tickets(self) -> List[str]:
        number_of_jira_tickets = random.randint(MIN_JIRA_TICKETS, MAX_JIRA_TICKETS)
        created_tickets_ids = []
        for i in range(0, number_of_jira_tickets):
            jira_ticket_data = random.choice(JIRA_TICKETS)
            created_tickets_ids.append(self._create_ticket(summary=jira_ticket_data['summary'],
                                                           description=jira_ticket_data['description'],
                                                           issuetype=jira_ticket_data['issuetype']))
        return created_tickets_ids

    def _create_ticket(self, summary: str, description: str, issuetype: str) -> str:
        issue_dict = {
            'project': {'key': self._project},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issuetype},
        }
        try:
            return str(self._connection.create_issue(fields=issue_dict))
        except Exception as e:
            print(e)
