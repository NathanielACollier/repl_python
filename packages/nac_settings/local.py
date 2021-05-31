
import json, os

def get(key: str)-> str:
    settingsFilePath = os.path.expanduser('~/settings.json')
    with open(settingsFilePath) as json_file:
        data = json.load(json_file)
        return data[key]



