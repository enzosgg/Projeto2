from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    CPF = models.CharField(max_length=11)
    Senha = models.TextField(max_length=128)
    Nome = models.TextField(max_length=50)
    telefone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)

class Consulta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateField()
    hora = models.TimeField()
    medico = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=50)
    local = models.CharField(max_length=100) 
    endereco = models.CharField(max_length=200) 

