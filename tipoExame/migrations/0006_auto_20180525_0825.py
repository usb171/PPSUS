# Generated by Django 2.0.2 on 2018-05-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipoExame', '0005_auto_20180524_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoexame',
            name='descricao',
            field=models.TextField(max_length=5000, null=True, verbose_name='Descricao'),
        ),
    ]
