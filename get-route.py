from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def get_response():
    with open('response.json') as file:
        data = json.load(file)
    return data