# fastapi-github-oauth
An isolated example to show github authorization-code oauth flow in fastapi for 
**web application flow** + **simple HttpBearer route dependency**.

## general information
* [building-oauth-apps](https://docs.github.com/en/developers/apps/building-oauth-apps)
* [fastAPI](https://fastapi.tiangolo.com)
* [fastapi/issues/12](https://github.com/tiangolo/fastapi/issues/12#issuecomment-457706256)

## create some github oauth app
* Log into github
* Settings > Developer Settings > Oauth Apps > New oauth App
* Fill out the form
  * `<some-name>`
  * `http://localhost:8000`
  * `<some-description>`
  * `http://localhost:8000/auth/login`
* Generate a ClientSecret (and don't paste it anywhere)
* Copy `ClientID` & `ClientSecret`
* Add your required scopes from [https://docs.github.com/](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps)
* Put it into and `.env`
* Take a look at the github documentation @ [https://docs.github.com/](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)

## web application flow
> The device flow isn't covered here at all. This example shows a simple web application flow using fastapis onboard utilities.

1. Request user permissions for provided scopes (`/auth/request`)
  * Let your user authenticate the github oauth app permission request
  * Github will forward to your `CALLBACK_URL` (`/auth/login`)
2. Recieve code from github and use it to provide the satisfied `acces_token` (`/auth/login`)
3. Use the recieved `acces_token` from step 2 to verify it using the Github API 
  * Output look like: `{"Id":<UserId>,"Login":"<GithubLogin>","Token":"<UserToken>","Message":"Happy hacking :D"}`

## securing routes with a dependency
* Use `HttpBearer`, to bear the token and use it as dependency for our routes
* These routes are only accessible for authenticated users (requests with valid `access_token`) 
* See the example with `secure/content`

## example

### Install stuff with [poetry](https://python-poetry.org)
```bash
git clone git@github.com:arrrrrmin/fastapi-github-oauth.git
cd fastapi-github-oauth
poetry install
poetry shell
uvicorn app.main:app --reload
```

### A _very_ minimalistic example
* Do the setup for your Oauth application [create some github oauth app](#create-some-github-oauth-app)
* Do API setup stuff with [Install stuff with poetry](#Install-stuff-with-poetry)
* Open the file in `examples/example.html`
* Click the link
* Happy hacking 🎉
