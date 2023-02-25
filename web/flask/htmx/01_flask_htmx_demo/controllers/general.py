from flask import Blueprint, render_template
from datetime import datetime

general_bp = Blueprint("general_blueprint", __name__)

@general_bp.route("/currentTime")
def getCurrentTime():
    now = datetime.now()
    return f'''
        <div>
            {now}
        </div>
    '''