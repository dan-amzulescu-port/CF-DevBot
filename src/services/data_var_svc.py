import ast
import json
import os
import random

from dotenv import load_dotenv

from constants import JSON_DATA_FILE, SECRETS_FILE


def get_random_app_service_name_and_id() -> tuple[str, int]:
    num_of_services = int(os.environ['APP_SERVICES_COUNT'])
    if num_of_services > 0:
        selected_service_id = random.randint(0, num_of_services - 1)
        app_services_list = ast.literal_eval(os.environ['APP_SERVICES_LIST'])
        return app_services_list[selected_service_id], selected_service_id
    return "", 0


class DataVarService:
    def __init__(self, json_data_file: str = JSON_DATA_FILE, env_secrets_file: str = SECRETS_FILE):
        self._json_data_file = json_data_file
        self._env_secrets_file = env_secrets_file
        try:
            self._load_data()
        except Exception as e:
            print(f"Error loading data environment: {e}")
            raise e

    def _load_data(self):
        if os.path.exists(self._env_secrets_file):
            load_dotenv(self._env_secrets_file)
        if os.path.exists(self._json_data_file):
            with open(self._json_data_file, 'r') as file:
                data = json.load(file)
        else:
            raise ValueError(f"No App Data Json file found: value given={self._json_data_file}")
        # Iterate through the keys in the JSON data
        for key in data.keys():
            # This enables override of json file using environment variables
            if key not in os.environ or not os.environ[key]:
                # Set each key as an environment variable with the same name as the key
                os.environ[key] = str(data[key])
