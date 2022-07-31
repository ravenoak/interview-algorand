from typing import Union

from pydantic import BaseSettings

CONFIGS: Union["Settings", None] = None


class Settings(BaseSettings):
    gh_token: str
    gh_user: str

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


def get_config() -> Settings:
    global CONFIGS
    if CONFIGS is None:
        CONFIGS = Settings()
    return CONFIGS
