from flask import Flask
from os import path
app = Flask(__name__)



def initFlaskSecret(app):
    googlePath = path.dirname(path.realpath(__file__))+ "\..\..\\flaskSecret.txt";
    with open(googlePath) as f: s = f.read()
    app.config['SECRET_KEY'] = s;


initFlaskSecret(app);


from app import SmartAlarm
from app import NofityMyAndorid
