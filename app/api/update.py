from flask import request
from flask_restful import Resource
from peewee import IntegrityError

from app.exceptions import InvalidEmailError, ShortPasswordError
from app.models import User
from app.responses import create_error_response, create_success_response
from app.schemas import SchemaUser


class Update(Resource):
    def patch(self, id):
        '''Atualiza os dados de um usuário no banco de dados.'''
        try:
            new_data = SchemaUser(**request.json)
            user = User.select().where(User.id == id).get()
            user.update_all(**new_data.dict())

            return create_success_response('Dados atualizados')

        except InvalidEmailError:
            return create_error_response('Email inválida')

        except ShortPasswordError:
            return create_error_response('Senha com menos de 6 caracteres')

        except IntegrityError:
            return create_error_response(
                'Email já registrado',
            )

        except User.DoesNotExist:
            return create_error_response('id não encontrado')
