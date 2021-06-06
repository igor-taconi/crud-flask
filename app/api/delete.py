from flask_restful import Resource

from app.models import User
from app.responses import create_error_response, create_success_response


class Delete(Resource):
    def delete(self, id):
        '''Deleta um usuário do banco de dados.'''
        user = User.delete_by_id(id)
        if user:
            return create_success_response('Excluido com sucesso')

        return create_error_response('Id não encontrado')
