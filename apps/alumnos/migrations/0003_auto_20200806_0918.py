# Generated by Django 3.0.8 on 2020-08-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20190620_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='rut',
            field=models.CharField(help_text='Indique su RUT', max_length=13, verbose_name='Id'),
        ),
    ]