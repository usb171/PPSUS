# Generated by Django 2.0.2 on 2018-05-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coleta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleta',
            name='pontuacao',
            field=models.CharField(blank=True, choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default='None', max_length=10, null=True, verbose_name='Pontuacao'),
        ),
    ]
