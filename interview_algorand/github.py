import logging

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

from . import config


def get_issues(repo: str, settings: config.Settings) -> dict:
    """Get the open issues for the given repo."""
    logger = logging.getLogger(__name__)

    # Defaults to 'open', but since the requirements for this exercise said
    # 'open', we'll explicitly set it to 'open'.
    # See: https://docs.github.com/en/rest/issues/issues#list-repository-issues
    url = f'https://api.github.com/repos/{repo}/issues?state=open'
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
