# Generated by Django 2.2.2 on 2019-06-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='nombre_eval',
            field=models.CharField(help_text='Descripcion de Evaluacion', max_length=200, verbose_name='Descripcion'),
        ),
    ]
