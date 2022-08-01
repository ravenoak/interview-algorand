import argparse
from typing import Union

from pydantic import BaseSettings

CONFIGS: Union["Settings", None] = None


class Settings(BaseSettings):
    """Settings for the program.

    This is a Pydantic model, so it can be used to validate the settings.

    gh_url: The base URL for the GitHub API.
    gh_user: The username for the GitHub API.
    gh_token: The token for the GitHub API.
    """

    debug: bool = False
    repo: str = "algorand/go-algorand"
    gh_token: str
    gh_user: str
    gh_url: str = "https://api.github.com"

    class Config:
        env_prefix = 'ALGORAND_'
        env_file = '.env'
        strict = True
        fields = {
            'gh_token': {
                'required': True,
            },
            'gh_user': {
                'required': True,
            },
        }


def get_config(args: argparse.Namespace) -> Settings:
    """Get the global config instance.

    If it doesn't exist, create it.
    """
    global CONFIGS
    if CONFIGS is None:
        CONFIGS = Settings(**vars(args))
    return CONFIGS
