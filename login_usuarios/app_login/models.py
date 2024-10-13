from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    CPF = models.CharField(max_length=11)
    Senha = models.TextField(max_length=128)
