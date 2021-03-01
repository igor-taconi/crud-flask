from flask import Flask
# from .model import session


def create_app():
    # instânciando o Flask
    app = Flask(__name__)

    from .routes import load

    load(app)

    # @app.teardown_request
    # def remove_session(ex=None):
    #     session.remove()

    return app
