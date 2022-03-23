from django.test import Client
import pytest


pytestmark = [pytest.mark.django_db]


def test_deve_criar_usuario(client: Client):
    data_requests = {
        "login": 'Michelle',
        "senha": "123",
        "data_nascimento": "2022-03-23",

    }

    response = client.post(path='/api/v1/usuario', data=data_requests)

    assert response.status_code == 201

    assert response.data['mensagem'] == 'Usuário cadastrado com sucesso'
    assert response.data['dados'] == {
        'id': 1,
        'login': 'Michelle',
        'senha': '123',
        'data_nascimento': '2022-03-23'
    }


def test_deve_criar_usuario_com_senha_aleatoria(client: Client):
    data_requests = {
        "login": 'Michelle',
        "data_nascimento": "2022-03-23"
    }

    response = client.post(path='/api/v1/usuario', data=data_requests)

    assert response.status_code == 201

    response_mensagem = response.data['mensagem']
    assert response_mensagem == 'Usuário cadastrado com sucesso'
    assert response.data['dados']['login'] == 'Michelle'
    assert response.data['dados']['senha'] is not None
    assert response.data['dados']['data_nascimento'] == '2022-03-23'
