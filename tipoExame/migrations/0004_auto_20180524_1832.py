# Generated by Django 2.0.2 on 2018-05-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoExame', '0003_auto_20180524_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoexame',
            name='pontuacao_limite',
        ),
        migrations.AddField(
            model_name='tipoexame',
            name='pontuacao_maxima',
            field=models.CharField(blank=True, choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default='None', max_length=10, null=True, verbose_name='Pontuação máxima'),
        ),
        migrations.AddField(
            model_name='tipoexame',
            name='pontuacao_minima',
            field=models.CharField(blank=True, choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default='None', max_length=10, null=True, verbose_name='Pontuação mínima'),
        ),
    ]
