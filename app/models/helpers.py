from typing import Any, Union, List, Optional
from requests import request
from urllib.parse import urlencode

from pydantic import BaseModel, BaseSettings, HttpUrl, validator


class GithubToken(BaseModel):
    access_token: str

    @validator("access_token")
    def validate_access_token(cls, v):
        if not v.startswith("gho_"):
            return ValueError(v)
        return v


class GithubTokenRespone(GithubToken):
    token_type: str
    scope: str

    @validator("token_type")
    def validate_token_type(cls, v):
        if v != "bearer":
            return ValueError(v)
        return v


class AuthorizedResponse(GithubToken):
    id: int
    login: str

    @validator("login")
    def validate_login(cls, v):
        if not len(v) > 0:
            return ValueError(v)
        return v

    @validator("id")
    def validate_id(cls, v):
        if not v > 0:
            return ValueError(v)
        return v


class GithubUser(BaseModel):
    id: int
    login: str
    node_id: str
    url: HttpUrl
    html_url: HttpUrl
    gists_url: HttpUrl
    starred_url: HttpUrl
    subscriptions_url: HttpUrl
    organizations_url: HttpUrl
    repos_url: HttpUrl
    events_url: HttpUrl
    received_events_url: HttpUrl
    type: str
    site_admin: bool
    name: Optional[str]
    company: Optional[str]
    # ...