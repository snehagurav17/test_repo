"""This program is test the pylint package."""
import json
import time
from flask import Flask
from flask import request



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    """Function for home page"""
    data_set = {'Page': 'Home', 'Message': 'Welcome to Home Page', 'CurrentTimeStamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    """Function for request page"""
    user_query = str(request.args.get('user'))  # /user/?user=username

    data_set = {'Page': 'Request',
                'Message': f'Hello user {user_query}',
                'CurrentTimeStamp': time.localtime()}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port=5555)
