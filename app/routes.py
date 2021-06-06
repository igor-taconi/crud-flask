from flask import Blueprint, request
from peewee import IntegrityError

from app.exceptions import InvalidEmailError, ShortPasswordError
from app.schemas import SchemaUser
from .model import User

bp = Blueprint('crud', __name__)


@bp.route('/')
def index():
    """Retorna a função como key e a rota como valor."""
    return {
        'criar': '/create',
        'ler': '/read',
        'atualizar': '/update<int:id>',
        'deletar': '/delete<int:id>',
    }


@bp.route('/create', methods=['POST'])
def create():
    """Insere um novo usuário no banco de dados."""
    try:
        user = SchemaUser(**request.json)

        User.create(**user.dict())
        return {'status': 201, 'mensagem': 'dados inseridos'}, 201
    except InvalidEmailError:
        return {'status': 400, 'mensagem': 'email inválida'}, 400
    except ShortPasswordError:
        return {
            'status': 400,
            'mensagem': 'Senha com menos de 6 caracteres',
        }, 400
    except IntegrityError:
        return {
            'status': 400,
            'mensagem': 'Email já registrado',
        }, 400


@bp.route('/read', methods=['GET'])
def read():
    """Retorna os dados dos usuários da banco de dados."""
    query = User.select().namedtuples()
    users = {
        user.id: {
            "username": user.username,
            "email": user.email,
            "password": user.password,
        }
        for user in query
    }

    return users, 200


@bp.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    """Atualiza os dados de um usuário no banco de dados."""

    try:
        user = User.select().where(User.id == id).get()
        new_data = SchemaUser(**request.json)
        user.username = new_data.username
        user.email = new_data.email
        user.password = new_data.password
        user.save()
        return {'status': 200, 'mensagem': 'dados atualizados'}, 200
    except InvalidEmailError:
        return {'status': 400, 'mensagem': 'email inválida'}, 400
    except ShortPasswordError:
        return {
            'status': 400,
            'mensagem': 'Senha com menos de 6 caracteres',
        }, 400
    except IntegrityError:
        return {
            'status': 400,
            'mensagem': 'Email já registrado',
        }, 400
    except User.DoesNotExist:
        return {'status': 404, 'mensagem': 'id não encontrado'}, 404


@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    """Deleta um usuário do banco de dados."""
    user = User.delete_by_id(id)
    if user:
        return {'status': 200, 'mensagem': 'exluido com sucesso'}, 200

    return {'status': 404, 'mensagem': 'id não encontrado'}, 404


def init_app(app):
    app.register_blueprint(bp)
