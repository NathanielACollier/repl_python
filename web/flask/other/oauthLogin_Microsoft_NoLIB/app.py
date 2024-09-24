from flask import Flask, redirect, url_for, session, request
from requests.models import PreparedRequest
import requests
import os
import nac_settings

# -- Run --
# python -m pip install -r requirements.txt
# python -m flask run

app = Flask(__name__)
app.secret_key = os.urandom(24) # This is critical because the authlib uses session, and you have to have a secret_key set for session


settings = {
    "msClientId": nac_settings.local.get("TestAuthAzureAppID"),
    "msClientSecret": nac_settings.local.get("TestAuthAzureClientSecret"),
    "redirectUri":"http://localhost:5000/auth",
    "tenant": "common",
    "graphScope":"User.Read"
}

@app.route('/')
def index():
    return '<h1>Welcome to the Flask App</h1>' + '<a href="/msLogin">Login with Microsoft</a>'

@app.route('/msLogin')
def login():
    redirect_uri = url_for('codeInput', _external=True)
    url = f"https://login.microsoftonline.com/{settings["tenant"]}/oauth2/v2.0/authorize"
    params = {
        "client_id": settings["msClientId"],
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "response_mode":"query",
        "scope": settings["graphScope"],
        "state":""
    }

    req = PreparedRequest()
    req.prepare_url(url, params)

    return redirect(req.url, code=307)



@app.route('/codeInput')
def codeInput():
    code = request.args.get("code")
    
    token = getToken(code)

    user = getCurrentUser(token)

    return f"Hello, {user["displayName"]} ({user["userPrincipalName"]}!"



def getToken(code: str)-> str:
    redirect_uri = url_for('codeInput', _external=True)

    resp = requests.post(f"https://login.microsoftonline.com/{settings["tenant"]}/oauth2/token",
                    data={
                        "grant_type": "authorization_code",
                        "client_id": settings["msClientId"],
                        "redirect_uri": redirect_uri,
                        "resource": "https://graph.microsoft.com",
                        "code": code,
                        "client_secret": settings["msClientSecret"]
                    }
                )
    
    if resp.status_code != 200:
        raise Exception(resp.text)
    
    obj = resp.json()
    return obj["access_token"]


def getCurrentUser(token: str)-> dict:

    resp = requests.get("https://graph.microsoft.com/v1.0/me",
                        headers={
                            "Authorization": f"Bearer {token}"
                        })
    
    if resp.status_code != 200:
        raise Exception(resp.text)
    
    obj = resp.json()
    return obj

if __name__ == '__main__':
    app.run(debug=True)