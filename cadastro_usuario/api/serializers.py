import string
from random import choice

from rest_framework.serializers import ModelSerializer

from cadastro_usuario.api.models import Usuario


class UserSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'

    def validate(self, data):
        if data.get('senha') is None:
            senha = gerar_senha_aleatoria()
            data['senha'] = senha
        return data


def gerar_senha_aleatoria():
    tamanho = 10

    senha = ''
    for i in range(tamanho):
        senha += choice(string.printable)

    return senha
