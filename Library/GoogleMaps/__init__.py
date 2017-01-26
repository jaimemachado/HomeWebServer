from flask import Flask
from os import path
from app import app

def initGoogle(app):
    googlePath = path.dirname(path.realpath(__file__))+ "/../../../googleKey.txt";
    with open(googlePath) as f: s = f.read()
    app.config['GOOGLE_KEY'] = s;

initGoogle(app);