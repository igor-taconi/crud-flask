from flask_restful import Resource

from app.responses import create_success_response


class Index(Resource):
    def get(self):
        '''Retorna a função como key e a rota como valor.'''
        info = {
            'criar': '/create',
            'ler': '/read',
            'atualizar': '/update<int:id>',
            'deletar': '/delete<int:id>',
        }

        return create_success_response(message='Ok', extra_info={'info': info})
