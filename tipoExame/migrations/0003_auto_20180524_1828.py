# Generated by Django 2.0.2 on 2018-05-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoExame', '0002_tipoexame_pontuacao_limite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoexame',
            name='pontuacao_limite',
            field=models.CharField(blank=True, choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default='0', max_length=10, null=True, verbose_name='Pontuação Limite'),
        ),
    ]
