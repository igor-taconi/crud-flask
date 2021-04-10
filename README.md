# CRUD com Flask

Experiência com um CRUD usando flask.

## Pré-requisitos
Para você rodar o projeto é necessário tem instalado em sua máquina o `Python3.6+`.

## Como rodar esse projeto
- ### Clone esse repositório.
```sh
git clone https://github.com/igor-taconi/crud-flask.git <nome_da_pasta>
```

- ### Crie um virtualenv com Python 3.
```sh
cd <nome_da_pasta>
python -m venv .venv
```

- ### Ative o virtualenv.
```sh
source .venv/bin/activate
```

- ### Instale as dependências.
```sh
pip install -r requirements.txt
```

- ### Como rodar esse projeto
```sh
flask run
```

ou

```sh
gunicorn app.wsgi:app --bind 0.0.0.0:5000 --timeout 100 --reload
```

### Exemplo de POSTs
```sh
{
  'username': 'Roberta',
  'email': 'robertaS2@gmail.com',
  'password': 'q1w2e3'
}
```

### Como usar
- No endereço pricipal há um mapa das postas  de suas funções. 'http://127.0.0.1:5000/'
- Para cadastrar um usuário envie o seu POST para a rota '/create'
- O username e o email são valores únicos para todos os usuários, não pode ter dois POSTs como o mesmo username e o mesmo email.
- A senha deve conter exatamente 6 caracteres.
- Para atualizar via '/update/<id\>' é necessário informar o ID do usuário na rota depois da barra '/'.
- Para excluir é necessário fazer GET para a rota '/delete/<id\>' e informar o ID do usuário depois do barra.
- Para ver os usuários que estão cadastrados basta acesse '/read'

## Contribuindo
Sinta-se à vontade para enviar pull requests.
