from .model import session, User
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

bp = Blueprint('crud', __name__)


def validate_data(data):
    if 'username' not in data.keys():
        return {'status': 400, 'mensagem': 'username não foi inserido'}, 400
    elif 'email' not in data.keys():
        return {'status': 400, 'mensagem': 'email não foi inserido'}, 400
    elif 'password' not in data.keys():
        return {'status': 400, 'mensagem': 'password não foi inserido'}, 400
    elif '@' not in data['email']:
        return {'status': 400, 'mensagem': 'email inválida'}, 400
    elif len(data['password']) != 6:
        return {
            'status': 400,
            'mensagem': 'o password deve ter 6 catacteres',
        }, 400


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
        user = request.get_json()
        validate_data(user)
        db_user = User(**user)
        session.add(db_user)
        session.commit()
        return {'status': 201, 'mensagem': 'dados inseridos'}, 201
    except IntegrityError as e:
        return {
            'status': 409,
            'mensagem': f'dados já existentes {e.orig}',
        }, 409


@bp.route('/read', methods=['GET'])
def read():
    """Retorna os dados dos usuários da banco de dados."""
    query = session.query(User).all()
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
        user = session.query(User).get(id)
        new_data = request.get_json()
        validate_data(new_data)
        user.username = new_data['username']
        user.email = new_data['email']
        user.password = new_data['password']
        session.commit()
        return {'status': 200, 'mensagem': 'dados atualizados'}, 200
    except IntegrityError as e:
        return {
            'status': 409,
            'mensagem': f'dados já existentes {e.orig}',
        }, 409
    except AttributeError:
        return {'status': 404, 'mensagem': 'id não encontrado'}, 404


@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    """Deleta um usuário do banco de dados."""
    try:
        user = session.query(User).get(id)
        session.delete(user)
        session.commit()
        return {'status': 200, 'mensagem': 'exluido com sucesso'}, 200
    except UnmappedInstanceError:
        return {'status': 404, 'mensagem': 'id não encontrado'}, 404


def init_app(app):
    app.register_blueprint(bp)
