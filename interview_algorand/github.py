import logging

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

from . import config


def get_issues(repo: str, settings: config.Settings) -> dict:
    """Get the issues for the given repo."""
    logger = logging.getLogger(__name__)

    url = f'https://api.github.com/repos/{repo}/issues'
    try:
        logger.debug(f'GET {url}')
        response = requests.get(
            url,
            auth=HTTPBasicAuth(settings.gh_user, settings.gh_token),
            headers={'Accept': 'application/vnd.github+json'})
    except HTTPError as e:
        logger.error(e)
        return {}
    return response.json()
