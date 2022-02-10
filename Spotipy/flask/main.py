from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=27015, debug=True)
    with app.app_context():
        from Spotipy.flask.routes import *
