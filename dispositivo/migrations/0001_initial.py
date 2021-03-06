# Generated by Django 2.0.2 on 2018-05-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, null=True, unique=True, verbose_name='Nome')),
                ('codigo', models.CharField(max_length=10, null=True, unique=True, verbose_name='Código')),
                ('uso', models.BooleanField(default=False)),
                ('visivel', models.BooleanField(default=False)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('dataModificacao', models.DateTimeField(auto_now_add=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
