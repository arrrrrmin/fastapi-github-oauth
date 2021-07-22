from functools import lru_cache
from typing import Dict

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer

from .config.settings import Settings

from app.auth.github import Github
from app.models import helpers


app = FastAPI()
auth = Github()


@lru_cache()
def get_settings():
    return Settings()


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="/request/login",
    tokenUrl="/secure/content",
    scopes=get_settings().get_scopes_as_map(),
    auto_error=True
)


@app.get("/")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "App": settings.APP_NAME,
        "Description": settings.APP_DESCRIPTION
    }


@app.get("/auth/request", response_class=RedirectResponse, status_code=302)
async def request_login():
    """ Route to redirect front end clients. """
    return auth.get_init_auth_url()


@app.get("/auth/login", response_model=Dict)
async def auth_login(code: str):
    """ Callback from oauth provider. """
    token = auth.get_access_token(code)
    user = auth.get_user_data(token.access_token)
    return {
        "Id": user.id,
        "Login": user.login,
        "Token": token.access_token,
        "Message": "Happy hacking :D"
    }


@app.get("/secure/content", response_model=Dict)
async def secure_route(user: helpers.AuthorizedResponse = Depends(auth.authorized_user)):
    """ Secure route with an authenticated user as route dependency. """
    return {
        "You": user,
        "Message": "Nice, your authorized 🎉"
    }
