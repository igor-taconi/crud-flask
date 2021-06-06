from flask import request
from flask_restful import Resource
from peewee import IntegrityError

from app.exceptions import InvalidEmailError, ShortPasswordError
from app.models import User
from app.responses import create_error_response, create_success_response
from app.schemas import SchemaUser


class Create(Resource):
    def post(self):
        '''Insere um novo usuário no banco de dados.'''
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
