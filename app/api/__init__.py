from typing import NoReturn

from flask import Blueprint, Flask
from flask_restful import Api

from app.api.create import Create
from app.api.delete import Delete
from app.api.index import Index
from app.api.read import Read
from app.api.update import Update

bp = Blueprint('crud', __name__, url_prefix='/api/v2')
api = Api(bp)

api.add_resource(Create, '/create')
api.add_resource(Delete, '/delete/<int:id>')
api.add_resource(Index, '/')
api.add_resource(Read, '/read')
api.add_resource(Update, '/update/<int:id>')


def init_app(app: Flask) -> NoReturn:
    app.register_blueprint(bp)
