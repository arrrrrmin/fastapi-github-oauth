from typing import Union

from pydantic import BaseSettings, HttpUrl, validator


class Settings(BaseSettings):
    APP_NAME: str
    APP_DESCRIPTION: str
    HOME_URL: Union[str, HttpUrl]
    CALLBACK_URL: Union[str, HttpUrl]
    CLIENT_ID: str
    CLIENT_SECRET: str
    SCOPE: str

    class Config:
        env_file = ".env"

    def get_scope_as_map(self):
        return {
            scope: scope
            for scope in self.SCOPE.split(" ")
        }
