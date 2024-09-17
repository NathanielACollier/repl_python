
from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os
import nac_settings

# -- Run --
# python -m pip install -r requirements.txt
# python -m flask run

# -- NOtes --
# original code from: https://medium.com/@tempmailwithpassword/integrate-flask-web-apps-with-microsoft-365-login-ae171d7b2164

app = Flask(__name__)

oauth = OAuth(app)

settings = {
    "msClientId": nac_settings.local.get("TestAuthAzureAppID"),
    "msClientSecret": nac_settings.local.get("TestAuthAzureClientSecret"),
    "redirectUri":"http://localhost:5000/auth"
}

oauth.register(
    name='microsoft',
    client_id=settings["msClientId"],
    client_secret=settings['msClientSecret'],
    authorize_url='https://login.microsoftonline.com/common/oauth2/v2.0/authorize',
    authorize_params=None,
    access_token_url='https://login.microsoftonline.com/common/oauth2/v2.0/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri=settings['redirectUri'],
    client_kwargs={'scope': 'User.Read'}
)


@app.route('/')
def index():
    return '<h1>Welcome to the Flask App</h1>' + '<a href="/msLogin">Login with Microsoft</a>'

@app.route('/msLogin')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.microsoft.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    token = oauth.microsoft.authorize_access_token()
    user = oauth.microsoft.parse_id_token(token)
    session['user'] = user
    return f'Hello, {user["name"]}!'

if __name__ == '__main__':
    app.run(debug=True)