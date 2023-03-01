from flask import Flask, send_from_directory, render_template
import os
from controllers.general import general_bp

# run this application with `python3 -m flask run`

# flask routes in a seperate file
#   see: https://stackoverflow.com/questions/66415003/how-to-import-routes-from-other-file-using-flask


app = Flask(__name__)

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")

app.register_blueprint(general_bp, url_prefix="/general")

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(root, path)


@app.route('/', methods=['GET'])
def redirect_to_index():
    #return send_from_directory(root, 'index.html')
    return render_template("pages/general/test1.html")


