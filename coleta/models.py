from django.db import models
from tipoExame.models import TipoExame
from paciente.models import Paciente


class Coleta(models.Model):

    _QUEDA_RISCO_CHOICES = (
        ('ALTO', 'alto'),
        ('MEDIO', 'médio'),
        ('BAIXO', 'baixo'),
    )
    _PONTUACAO_CHOICES = (
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),
    )

    numero_exec = models.PositiveSmallIntegerField(default=0)
    tipoExame = models.ForeignKey(TipoExame, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    observacao  = models.TextField('Observação', max_length=200, blank=True, null=True)



    riscoQueda = models.CharField('Risco de Queda', max_length=10, choices=_QUEDA_RISCO_CHOICES, default="None", blank=True, null=True)
    pontuacao = models.CharField('Pontuacao', max_length=10, choices=_PONTUACAO_CHOICES, default="None", blank=True, null=True)
    pontuacao_soma = models.CharField('Pontuacao Soma', max_length=10, blank=True, null=True)
    cronometro = models.CharField('Tempo', max_length=10, blank=True, null=True)
    deslocamento = models.CharField('Deslocamento cm', max_length=10, blank=True, null=True)


    visivel = models.BooleanField(default=False)
    amostras = models.TextField(blank=True, null=True)

    dataCriacao = models.DateTimeField('Criado em', auto_now_add=True)
    dataModificacao = models.DateTimeField('Atualizado em', auto_now_add=True)
