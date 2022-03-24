from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from cadastro_usuario.api.serializers import UserSerializer
from cadastro_usuario.api.models import Usuario


class UserView(GenericViewSet):
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={
                'mensagem': 'Usuário cadastrado com sucesso',
                'dados': serializer.data
            },
            status=201
        )

    def list(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(data=serializer.data, status=200)
