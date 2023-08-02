from flask import Flask, send_from_directory
import os

# run this application with `python3 -m flask run`

app = Flask(__name__)

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(root, path)


@app.route('/', methods=['GET'])
def redirect_to_index():
    return send_from_directory(root, 'index.html')


