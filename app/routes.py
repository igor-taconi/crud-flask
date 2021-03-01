from flask import Flask, request, jsonify
from .model import session, User
from .data_validate import validate_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


def load(app: Flask) -> Flask:
    @app.route('/')
    def index():
        """Retorna a função como key e a rota como valor."""
        return jsonify(
            {
                'criar': '/create',
                'ler': '/read',
                'atualizar': '/update<int:id>',
                'deletar': '/delete<int:id>',
            }
        )

    @app.route('/create', methods=['POST'])
    def create():
        """Insere um novo usuário no banco de dados."""
        try:
            user = request.get_json()
            validate_user(user)
            db_user = User(**user)
            session.add(db_user)
            session.commit()
            return (
                jsonify({'status': 201, 'mensagem': 'dados inseridos'}),
                201,
            )
        except IntegrityError as e:
            return (
                jsonify(
                    {
                        'status': 400,
                        'mensagem': f'dados já existentes {e.orig}',
                    }
                ),
                400,
            )

    @app.route('/read', methods=['GET'])
    def read():
        """Retorna os dados dos usuários da banco de dados."""
        users = [u.as_dict() for u in session.query(User).all()]
        return jsonify(users)

    @app.route('/update/<int:id>', methods=['POST'])
    def update(id):
        """Atualiza os dados de um usuário no banco de dados."""
        try:
            user = session.query(User).get(id)
            new_data = request.get_json()
            validate_user(new_data)
            user.username = new_data['username']
            user.email = new_data['email']
            user.password = new_data['password']
            session.commit()
            return (
                jsonify({'status': 201, 'mensagem': 'dados atualizados'}),
                201,
            )
        except IntegrityError as e:
            return (
                jsonify(
                    {
                        'status': 400,
                        'mensagem': f'dados já existentes {e.orig}',
                    }
                ),
                400,
            )
        except AttributeError:
            return (
                jsonify({'status': 400, 'mensagem': 'id não encontrado'}),
                400,
            )

    @app.route('/delete/<int:id>', methods=['GET'])
    def delete(id):
        """Deleta um usuário do banco de dados."""
        try:
            user = session.query(User).get(id)
            session.delete(user)
            session.commit()
            return (
                jsonify({'status': 200, 'mensagem': 'exluido com sucesso'}),
                200,
            )
        except UnmappedInstanceError:
            return (
                jsonify({'status': 400, 'mensagem': 'id não encontrado'}),
                400,
            )

    return app
