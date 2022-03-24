import factory

from cadastro_usuario.api.models import Usuario


class UsuarioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario

    login = 'Michelle'
    senha = '123'
    data_nascimento = '2022-03-23'
