# fastapi-github-oauth
An isolate example to provide a github oauth in fastapi

## create some Github Oauth App
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

