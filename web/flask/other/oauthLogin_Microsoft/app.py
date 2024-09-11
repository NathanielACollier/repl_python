
from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth
import os
import nac_settings

# -- Run --
# python -m venv venv
# source venv/bin/activate
# set -o allexport; source .env; set +o allexport
# python -m pip install -r requirements.txt
# python -m flask run

# -- NOtes --
# original code from: https://medium.com/@tempmailwithpassword/integrate-flask-web-apps-with-microsoft-365-login-ae171d7b2164

app = Flask(__name__)

oauth = OAuth(app)

microsoft = oauth.remote_app(
    'microsoft',
    consumer_key='YOUR_APP_ID',
    consumer_secret='YOUR_APP_SECRET',
    request_token_params={'scope': 'User.Read'}
    base_url='https://graph.microsoft.com/v1.0/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://login.microsoftonline.com/common/oauth2/v2.0/token',
    authorize_url='https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
)
@app.route('/')
def index():
    return '<h1>Welcome to the Flask App</h1>' + '<a href="/login">Login with Microsoft</a>'

@app.route('/login')
def login():
    return microsoft.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/authorized')
def authorized():
    response = microsoft.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={0} error={1}'.format(
            request.args['error'], request.args['error_description'])
    session['oauth_token'] = (response['access_token'], '')
    return 'Logged in as id={0}'.format(session['oauth_token'])

@microsoft.tokengetter
def get_microsoft_oauth_token():
    return session.get('oauth_token')

if __name__ == '__main__':
    app.run(debug=True)