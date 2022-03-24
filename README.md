# frexco-desafio-tech-cadastro-usuario
Construir pelo menos dois endpoints utilizando Django:   
  - Cadastrar usuário, fornecendo o login, senha e data de nascimento   
  - Senha deixar como opcional, se não fornecido gerar uma senha aleatória.   
  - Consultar usuários cadastrados.   
  - Deve ser possível consultar em XLSX, CSV ou JSON.

# Passo a passo para rodar a aplicação

Foi utilizado o Python 3.9

## Instalar dependências
```
pip install -r requirements-dev.txt
```

## Subir base de dados Postgres
```
docker-compose up -d
```

## Executar aplicação
```
python manage.py runserver
```

# Endpoints
- Url base da aplicação: `http://127.0.0.1:8000/api/v1/`
- Cadastrar usuário: POST - `http://127.0.0.1:8000/api/v1/usuario`
  - ```
    {
        "login": "teste",
        "senha": "123",
        "data_nascimento": "2022-03-24",
    }
    ```
  - A senha é opcional
- Listar usuário: GET - `http://127.0.0.1:8000/api/v1/usuario`


# Documentação da API
A documentação da api está disponível em `http://127.0.0.1:8000/swagger/`


# Convenções de código e testes
## Rodar convenção de código
```
flake8
```

## Rodar testes
```
pytest
```

Obs: Ambos foram implementados no CI (Github Actions)
