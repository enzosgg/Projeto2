from django.urls import path
from app_login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('usuarios/', views.usuarios_ou_perfil, name="listagem_usuarios"),
    path('usuarios/<int:usuario_id>/',
         views.usuarios_ou_perfil, name="listagem_usuarios_id"),
    path('perfil/<int:usuario_id>/',
         views.usuarios_ou_perfil, name="perfil_usuario"),
    path('consultainfo/<int:consulta_id>/',
         views.consulta_info, name="consultainfo"),
]
