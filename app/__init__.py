from flask import Flask
from os import path
app = Flask(__name__)



def initFlaskSecret(app):
    googlePath = path.dirname(path.realpath(__file__))+ "\..\..\\flaskSecret.txt";
    with open(googlePath) as f: s = f.read()
    app.config['SECRET_KEY'] = s;

def run_apps():
    app.config.from_object('config');
    app.run(debug=app.config['DEBUG'], host='0.0.0.0');


initFlaskSecret(app);


from app import SmartAlarm
from app import NofityMyAndorid
from app import ManageServer
