from flask import jsonify


def validate_user(user):
    if 'username' not in user.keys():
        return (
            jsonify({'status': 400, 'mensagem': 'username não foi inserido'}),
            400,
        )
    elif 'email' not in user.keys():
        return (
            jsonify({'status': 400, 'mensagem': 'email não foi inserido'}),
            400,
        )
    elif 'password' not in user.keys():
        return (
            jsonify({'status': 400, 'mensagem': 'password não foi inserido'}),
            400,
        )
    elif '@' not in user['email']:
        return jsonify({'status': 400, 'mensagem': 'email inválida'}), 400
    elif len(user['password']) != 6:
        return (
            jsonify(
                {'status': 400, 'mensagem': 'o password deve ter 6 catacteres'}
            ),
            400,
        )
