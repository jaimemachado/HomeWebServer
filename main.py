from app import app
from os import path
app.config.from_object('config');

def initGoogle(app):
    googlePath = path.dirname(path.realpath(__file__))+ "\..\googleKey.txt";
    with open(googlePath) as f: s = f.read()
    app.config['GOOGLE_KEY'] = s;

def initFlaskSecret(app):
    googlePath = path.dirname(path.realpath(__file__))+ "\..\\flaskSecret.txt";
    with open(googlePath) as f: s = f.read()
    app.config['SECRET_KEY'] = s;

if __name__ == "__main__":
    initGoogle(app);
    initFlaskSecret(app);
    app.run(debug = app.config['DEBUG']);