from django.db import models

class TipoExame(models.Model):


    _PONTUACAO_CHOICES = (
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),

    )

    nomeExame = models.CharField('Nome do Exame', max_length=30)
    descricao = models.TextField('Descricao', max_length=5000, null=True)

    # execucao = models.PositiveSmallIntegerField(default=1)
    visivel = models.BooleanField(default=True)

    pontuacao = models.BooleanField(default=False)
    pontuacao_minima = models.CharField('Pontuação mínima', max_length=10, choices=_PONTUACAO_CHOICES, default="0", blank=True, null=True)
    pontuacao_maxima = models.CharField('Pontuação máxima', max_length=10, choices=_PONTUACAO_CHOICES, default="0", blank=True, null=True)

    observacao = models.BooleanField(default=True)
    cronometro = models.BooleanField(default=True)
    risco_queda = models.BooleanField(default=False)
    deslocamento = models.BooleanField(default=False)
    pontuacao_soma = models.BooleanField(default=False)
    coleta_dispositivo = models.BooleanField(default=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now_add=True)

    def __str__(self):
        return self.nomeExame
