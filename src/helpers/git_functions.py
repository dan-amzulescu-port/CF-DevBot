import subprocess
from typing import Dict

import requests

from helpers.logging_functions import handle_success, handle_error


def validate_git_config_is_set() -> None:
    set_git_config('user.name', 'devbot')
    set_git_config('user.email', 'devbot@devbot.io')


def set_git_config(var_name, var_value):
    try:
        subprocess.check_output(['git', 'config', var_name])
        handle_success(f"Git configuration variable '{var_name}' is already configured.")
    except subprocess.CalledProcessError:
        print(f"Git configuration variable '{var_name}' is not configured.")
        # Set Git configuration variable
        subprocess.run(['git', 'config', '--global', var_name, var_value])
        print(f"Git configuration variable '{var_name}' has been set to '{var_value}'.")


def get_github_headers(token: str) -> Dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    }


def get_repo_data(url: str, token: str, data_key: str) -> str:
    headers = get_github_headers(token)
    response = requests.get(url, headers=headers)

    # Check if the response was successful
    if response.status_code == 200:
        handle_success(f"Repo {url} info was retrieved successfully")
        repo_info = response.json()
        return repo_info[data_key]
    else:
        handle_error(f"Repo {url} info was not retrieved successfully: HTTP {response.status_code}")
