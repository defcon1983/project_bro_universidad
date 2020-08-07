from django.db import models
from apps.profesores.models import Profesor

# Create your models here.
class Curso(models.Model):
    descripcion = models.CharField(max_length=100,help_text="Descripcion del Curso",verbose_name="Descripcion del Curso")
    
class RelacionCursoProfesor(models.Model):
    id_profesor = models.ForeignKey(Profesor,null=False,blank=False,on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)    


    

