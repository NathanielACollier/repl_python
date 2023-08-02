from flask import Blueprint, jsonify
from datetime import datetime

general_bp = Blueprint("general_blueprint", __name__)

buttonClickCounter = 0

@general_bp.route("/currentTime")
def getCurrentTime():
    now = datetime.now()
    return jsonify(now + "")

@general_bp.route("/buttonClick1")
def getButtonClick1():
    global buttonClickCounter
    buttonClickCounter += 1
    return jsonify(buttonClickCounter)





