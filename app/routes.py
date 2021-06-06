from flask import Blueprint, request
from peewee import IntegrityError

from app.exceptions import InvalidEmailError, ShortPasswordError
from app.responses import create_error_response, create_success_response
from app.schemas import SchemaUser
from .model import User

bp = Blueprint('crud', __name__)


@bp.route('/')
def index():
    """Retorna a função como key e a rota como valor."""
    info = {
        'criar': '/create',
        'ler': '/read',
        'atualizar': '/update<int:id>',
        'deletar': '/delete<int:id>',
    }

    return create_success_response(message='Ok', extra_info={'info': info})


@bp.route('/create', methods=['POST'])
def create():
    """Insere um novo usuário no banco de dados."""
    try:
        user = SchemaUser(**request.json)

        User.create(**user.dict())
        return create_success_response('Dados inseridos', status_code=201)

    except InvalidEmailError:
        return create_error_response('email inválida')

    except ShortPasswordError:
        return create_error_response('Senha com menos de 6 caracteres')

    except IntegrityError:
        return create_error_response('Email já registrado')


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

    return create_success_response(message='Ok', extra_info={'result': users})


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

        return create_success_response('Dados atualizados')

    except InvalidEmailError:
        return create_error_response('Email inválida')

    except ShortPasswordError:
        return create_error_response('Senha com menos de 6 caracteres')

    except IntegrityError:
        return create_error_response('Email já registrado',)

    except User.DoesNotExist:
        return create_error_response('id não encontrado')


@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    """Deleta um usuário do banco de dados."""
    user = User.delete_by_id(id)
    if user:
        return create_success_response('Excluido com sucesso')

    return create_error_response('id não encontrado')


def init_app(app):
    app.register_blueprint(bp)
