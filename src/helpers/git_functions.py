import logging
import subprocess
from typing import Dict
from bs4 import BeautifulSoup

import requests

from helpers.logging_functions import handle_success, handle_error


def validate_git_config_is_set(logger: logging.Logger) -> None:
    set_git_config('user.name', 'devbot', logger)
    set_git_config('user.email', 'devbot@devbot.io', logger)


def set_git_config(var_name, var_value, logger: logging.Logger) -> None:
    try:
        subprocess.check_output(['git', 'config', var_name])
        handle_success(f"Git configuration variable '{var_name}' is already configured.", logger)
    except subprocess.CalledProcessError:
        logger.warning(f"Git configuration variable '{var_name}' is not configured.")
        # Set Git configuration variable
        subprocess.run(['git', 'config', '--global', var_name, var_value])
        logger.debug(f"Git configuration variable '{var_name}' has been set to '{var_value}'.")


def get_github_headers(token: str) -> Dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    }


def get_default_branch(url: str, token: str, logger: logging.Logger) -> str:
    headers = get_github_headers(token)
    response = requests.get(url, headers=headers)

    # Check if the response was successful
    if response.status_code == 200:
        handle_success(f"Repo {url} info was retrieved successfully", logger)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        if not soup.find('span', {'class': 'css-truncate-target'}).text:
            handle_error("not able to determine repo default branch - html parser could not find it", logger)
        return soup.find('span', {'class': 'css-truncate-target'}).text
    else:
        handle_error(f"default branch for {url} was not retrieved successfully: HTTP {response.status_code}", logger)
