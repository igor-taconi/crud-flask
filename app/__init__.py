from flask import Flask

from app.settings import init_app


def create_app() -> Flask:
    app = Flask(__name__)

    init_app(app)

    app.config.load_extensions()

    return app
