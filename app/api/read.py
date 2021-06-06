from flask_restful import Resource

from app.models import User
from app.responses import create_success_response


class Read(Resource):
    def get(self):
        '''Retorna os dados dos usuários da banco de dados.'''
        users = User.get_all()

        return create_success_response(
            message='Ok', extra_info={'result': users}
        )
