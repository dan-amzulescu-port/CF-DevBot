import logging
import random
from typing import List

import requests
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
        self._jira_client = JIRA(basic_auth=(self._jira_data.jira_user_email, self._jira_data.jira_token),
                                 server=self._jira_data.jira_server)
        # TODO: enable jira feature below
        # self._get_jira_projects_users()

    def _get_jira_projects_users(self):

        # Define the REST API endpoint
        endpoint = f"{self._jira_data.jira_server}/rest/api/3/project/{self._jira_data.project}/role"

        # Make GET request to fetch project role details
        response = requests.get(endpoint, auth=(self._jira_data.jira_user_email,
                                                self._jira_data.jira_token))

        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            project_roles = response.json()

            # Fetch and print users for each project role
            for role_name, role_details in project_roles.items():
                if role_name == "Administrator":
                    role_url = role_details
                    role_response = requests.get(role_url,
                                                 auth=(self._jira_data.jira_user_email,
                                                       self._jira_data.jira_token))
                    if role_response.status_code == 200:
                        role_actors = role_response.json()['actors']
                        for actor in role_actors:
                            actor_type = actor['type']
                            actor_name = actor['name']
                            actor_display_name = actor['displayName']
                            if actor_type == 'atlassian-user-role-actor':
                                print(f"User: {actor_name} ({actor_display_name})")
                            elif actor_type == 'atlassian-group-role-actor':
                                print(f"Group: {actor_name} ({actor_display_name})")
                    else:
                        print(f"Failed to fetch actors for role {role_name}. Status code: {role_response.status_code}")
        else:
            print(f"Failed to fetch project roles. Status code: {response.status_code}")

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
            return str(self._jira_client.create_issue(fields=issue_dict))
        except Exception as e:
            logger.error("Error creating Jira Ticket: %s", e)
            raise e
