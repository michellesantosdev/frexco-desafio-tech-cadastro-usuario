from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


class UserView(GenericViewSet):

    def create(self, request):
        return Response(data={'mensagem': 'usuario cadastrado cm sucesso'}, status=201)
