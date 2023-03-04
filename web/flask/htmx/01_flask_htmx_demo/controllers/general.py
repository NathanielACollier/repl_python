from flask import Blueprint, render_template
from datetime import datetime

general_bp = Blueprint("general_blueprint", __name__)

buttonClickCounter = 0

@general_bp.route("/currentTime")
def getCurrentTime():
    now = datetime.now()
    return f'''
        <div>
            {now}
        </div>
    '''

@general_bp.route("/buttonClick1")
def getButtonClick1():
    global buttonClickCounter
    buttonClickCounter += 1
    return f'''
        <span style='color:red;font-weight:bold;'>You clicked the button {buttonClickCounter}</span>
    '''

@general_bp.route("/test1")
def getTest1():
    return render_template("pages/general/test1.html")

