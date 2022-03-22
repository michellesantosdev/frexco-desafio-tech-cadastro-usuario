from django.urls import path, include
from rest_framework_nested import routers

from cadastro_usuario.api.views import UserView


rota_usuario = routers.DefaultRouter(trailing_slash=False)
rota_usuario.register('usuario', UserView, basename='UserView')


app_name = 'api'


urlpatterns = (
    path('', include(rota_usuario.urls)),
)
