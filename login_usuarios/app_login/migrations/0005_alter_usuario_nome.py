# Generated by Django 5.0.2 on 2024-10-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0004_alter_usuario_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Nome',
            field=models.TextField(default='Desconhecido', max_length=50),
        ),
    ]