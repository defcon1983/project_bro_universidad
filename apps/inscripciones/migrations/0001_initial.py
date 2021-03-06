# Generated by Django 2.2.2 on 2019-06-15 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno')),
                ('id_relacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.RelacionCursoProfesor')),
            ],
        ),
    ]
