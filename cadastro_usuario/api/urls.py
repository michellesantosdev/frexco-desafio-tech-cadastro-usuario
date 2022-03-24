from django.urls import path, include
from rest_framework_nested import routers

from cadastro_usuario.api.views import UsuarioView


rota_usuario = routers.DefaultRouter(trailing_slash=False)
rota_usuario.register('usuario', UsuarioView, basename='UsuarioView')


app_name = 'api'


urlpatterns = (
    path('', include(rota_usuario.urls)),
)
