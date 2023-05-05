import logging
import random
from typing import List

import requests
from jira import JIRA

from blob_constants import JIRA_TICKETS

# Set up logging
from constants import JIRA_USER_ROLES
from model.jira_data import JiraData

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG


class JiraService:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._jira_data = JiraData()
        try:
            self._jira_client = self._create_jira_connection()
        except Exception as e:
            self._logger.error("Error creating Jira Connection: %s", e)
            raise e
        self._jira_users = self._get_jira_projects_users()

    def _create_jira_connection(self) -> JIRA:
        return JIRA(basic_auth=(self._jira_data.jira_user_email,
                                self._jira_data.jira_token),
                    server=self._jira_data.jira_server)

    def _get_jira_projects_users(self) -> List[str]:
        user_list = []
        # Define the REST API endpoint
        endpoint = f"{self._jira_data.jira_server}/rest/api/3/project/{self._jira_data.project}/role"

        # Make GET request to fetch project role details
        response = requests.get(endpoint, auth=(self._jira_data.jira_user_email, self._jira_data.jira_token))
        # Check if request was successful
        if response.status_code == 200:
            project_roles = response.json()
            # Fetch and print users for each project role
            for role_name, role_url in project_roles.items():
                if role_name in JIRA_USER_ROLES:
                    role_response = requests.get(role_url,
                                                 auth=(self._jira_data.jira_user_email,
                                                       self._jira_data.jira_token))
                    if role_response.status_code == 200:
                        for actor in role_response.json()['actors']:
                            if actor['type'] == 'atlassian-user-role-actor':
                                user_list.append(actor['actorUser']["accountId"])
                                self._logger.info(f"{actor['displayName']} was added to Jira Project users")
                    else:
                        self._logger.error(f"Failed to fetch actors for role {role_name}. "
                                           f"Status code: {role_response.status_code}")
        else:
            self._logger.error(f"Failed to fetch project roles. Status code: {response.status_code}")
        return user_list

    def create_jira_tickets(self) -> List[str]:
        number_of_jira_tickets = random.randint(self._jira_data.min_jira_tickets, self._jira_data.max_jira_tickets)
        created_tickets_ids = []
        for i in range(0, number_of_jira_tickets):
            jira_ticket_data = random.choice(JIRA_TICKETS)
            created_tickets_ids.append(self._create_ticket(summary=jira_ticket_data['summary'],
                                                           description=jira_ticket_data['description'],
                                                           issuetype=jira_ticket_data['issuetype'],
                                                           assignee=random.choice(self._jira_users)))
        return created_tickets_ids

    def _create_ticket(self, summary: str, description: str, issuetype: str, assignee: str) -> str:
        issue_dict = {
            'project': {'key': self._jira_data.project},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issuetype},
        }
        if len(self._jira_users) > 0:
            issue_dict.update({'assignee': {'accountId': assignee}})
        try:
            return str(self._jira_client.create_issue(fields=issue_dict))
        except Exception as e:
            self._logger.error("Error creating Jira Ticket: %s", e)
            raise e
