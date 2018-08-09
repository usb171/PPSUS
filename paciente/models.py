from django.db import models

class Paciente(models.Model):

    _SEXO_CHOICES = (
        ('MASCULINO', 'masculino'),
        ('FEMENINO', 'femenino'),
    )

    _NIVEL_ATIVIDADE_CHOICES = (
        ('MUITO_ATIVO', 'MUITO_ATIVO'),
        ('ATIVO', 'ATIVO'),
        ('IRREG_ATIVO_A', 'IRREG_ATIVO_A'),
        ('IRREG_ATIVO_B', 'IRREG_ATIVO_B'),
        ('SEDENTARISMO', 'SEDENTARISMO'),
    )

    code_nomeCompleto = models.CharField('código nome',  max_length=2, null=True)
    nomeCompleto = models.CharField('Nome', max_length=120)
    cpf = models.CharField(max_length=11, null=True)
    sexo = models.CharField('Sexo', max_length=10, choices=_SEXO_CHOICES, default="MASCULINO")
    nivelAtividade = models.CharField('Nivel Atividade', max_length=20, choices=_NIVEL_ATIVIDADE_CHOICES, default="SEDENTARISMO")

    telefone = models.CharField('Telefone', max_length=20, null=True)
    dataNascimento = models.DateField('Data de Nascimento', null=True)
    altura = models.FloatField('Altura', null=True)
    peso = models.FloatField('Peso', null=True)
    IMC = models.FloatField('IMC', null=True)
    observacao = models.TextField('Anotacoes', max_length=120, null=True)
    visivel = models.BooleanField(default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now_add=True)

    # class Meta:
    #     unique_together = ('nome', 'exame',)

    def __str__(self):
        return self.nomeCompleto
