from django.db import models

class Dispositivo(models.Model):

    nome = models.CharField('Nome', max_length=10, unique=True, null=True)
    codigo = models.CharField('Código',  max_length=10, unique=True, null=True)
    uso = models.BooleanField(default=False)
    visivel = models.BooleanField(default=False)

    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Atualizado em', auto_now_add=True)
