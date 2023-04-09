import logging
import random
from typing import List
from jira import JIRA

from blob_constants import JIRA_TICKETS

# Set up logging
from model.jira_data import JiraData

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG
logger = logging.getLogger(__name__)  # Create a logger for the current module


class JiraService:
    def __init__(self):
        self._jira_data = JiraData()
        try:
            self._create_jira_connection()
        except Exception as e:
            logger.error("Error creating Jira Connection: %s", e)
            raise e

    def _create_jira_connection(self):
        self._connection = JIRA(basic_auth=(self._jira_data.jira_user_email, self._jira_data.jira_token),
                                server=self._jira_data.jira_server)

    def create_jira_tickets(self) -> List[str]:
        number_of_jira_tickets = random.randint(self._jira_data.min_jira_tickets, self._jira_data.max_jira_tickets)
        created_tickets_ids = []
        for i in range(0, number_of_jira_tickets):
            jira_ticket_data = random.choice(JIRA_TICKETS)
            created_tickets_ids.append(self._create_ticket(summary=jira_ticket_data['summary'],
                                                           description=jira_ticket_data['description'],
                                                           issuetype=jira_ticket_data['issuetype']))
        return created_tickets_ids

    def _create_ticket(self, summary: str, description: str, issuetype: str) -> str:
        issue_dict = {
            'project': {'key': self._jira_data.project},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issuetype},
        }
        try:
            return str(self._connection.create_issue(fields=issue_dict))
        except Exception as e:
            logger.error("Error creating Jira Ticket: %s", e)
            raise e
