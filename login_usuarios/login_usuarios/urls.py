from django.urls import path
from app_login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('usuarios/', views.usuarios, name="listagem_usuarios"),
]
