from django.db import models
from paciente.models import Paciente
from coleta.models import Coleta
from django.utils.encoding import python_2_unicode_compatible

#
#
# class TipoExame(models.Model):
#     nomeExame = models.CharField('Nome do Exame', max_length=20)
#     created_at = models.DateTimeField('Criado em', auto_now_add=True)
#     update_at = models.DateTimeField('Atualizado em', auto_now_add=True)
#
#     def __str__(self):
#         return self.nomeExame

class Exame(models.Model):

    fk_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    fk_coleta = models.ManyToManyField(Coleta, blank=True)
    # fk_coleta = models.ForeignKey(Coleta, on_delete=models.CASCADE, null=True)
    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Atualizado em', auto_now_add=True)
