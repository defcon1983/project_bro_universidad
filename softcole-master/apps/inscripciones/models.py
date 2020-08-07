from django.db import models
from apps.alumnos.models import Alumno
from apps.cursos.models import RelacionCursoProfesor
from random import choices

# Create your models here.
class Inscripcion(models.Model):
    id_alumno = models.ForeignKey(Alumno,null=False,blank=False,
                                  on_delete=models.CASCADE)
    id_relacion = models.ForeignKey(RelacionCursoProfesor,null=False,
                                    blank=False,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)