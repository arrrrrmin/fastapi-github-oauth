import json
from requests import request
from urllib.parse import urlencode

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

from app.models import helpers
from app.config.settings import Settings


token_bearer = HTTPBearer(
    auto_error=True
)


class Github(BaseModel):

    INIT_AUTH_URL: str = "https://github.com/login/oauth/authorize"
    CODE_EXCH_URL: str = "https://github.com/login/oauth/access_token"
    USER_ENDP_URL: str = "https://api.github.com/user"
    settings: Settings = Settings()

    def get_init_auth_url(self):
        request_params = {"client_id": self.settings.CLIENT_ID}
        return "{0}/?{1}".format(self.INIT_AUTH_URL, urlencode(request_params))

    def get_access_token_from_code(self, code) -> helpers.GithubTokenRespone:
        request_data = {
            "client_id": self.settings.CLIENT_ID,
            "client_secret": self.settings.CLIENT_SECRET,
            "code": code,
        }
        return helpers.GithubTokenRespone(
            **json.loads(
                request(
                    method="post",
                    url=self.CODE_EXCH_URL,
                    headers={"Accept": "application/json"},
                    data=request_data
                ).text
            )
        )

    def get_user_data(self, token: str) -> helpers.AuthorizedResponse:
        return helpers.AuthorizedResponse(
            access_token=token,
            **json.loads(
                request(
                    method="get",
                    url=self.USER_ENDP_URL,
                    headers={"Authorization": "token {0}".format(token)}
                ).text
            )
        )

    def authorized_user(
        self, token: HTTPAuthorizationCredentials = Depends(token_bearer)
    ) -> helpers.AuthorizedResponse:
        user = self.get_user_data(token.credentials)
        return helpers.AuthorizedResponse(
            access_token=token.credentials,
            id=user.id,
            login=user.login,
        )