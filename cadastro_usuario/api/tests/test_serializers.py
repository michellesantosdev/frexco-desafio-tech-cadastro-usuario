import datetime
import pytest

from ..serializers import UserSerializer


pytestmark = [pytest.mark.django_db]


def test_deve_deserializar_usuario():
    dados_do_usuario = {
        'login': 'Michelle',
        'senha': '123',
        'data_nascimento': '2022-02-23',
        }

    usuario_serializado = UserSerializer(data=dados_do_usuario)
    usuario_serializado.is_valid()
    usuario_objeto = usuario_serializado.save()

    assert usuario_objeto.login == 'Michelle'
    assert usuario_objeto.senha == '123'
    assert usuario_objeto.data_nascimento == datetime.date(2022, 2, 23)


def test_deve_serializer_usuario(usuario):
    usuario_serializado = UserSerializer(usuario)

    assert usuario_serializado.data['login'] == 'Michelle'
    assert usuario_serializado.data['senha'] == '123'
    assert usuario_serializado.data['data_nascimento'] == '2022-03-23'
