from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import load

    load(app)

    return app
