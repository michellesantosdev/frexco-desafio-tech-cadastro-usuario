import pytest

from ..models import Usuario


pytestmark = [pytest.mark.django_db]


def test_deve_criar_usuario(usuario):
    assert Usuario.objects.count() == 1
    assert usuario.login == 'Michelle'
    assert usuario.senha == '123'
    assert usuario.data_nascimento == '2022-03-23'
