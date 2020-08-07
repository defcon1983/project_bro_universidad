from django.db import models
from apps.cursos.models import RelacionCursoProfesor

# Create your models here.
class Evaluacion(models.Model):
    SCORE_CHOICES = zip( range(1,100), range(1,100) )
    nombre_eval = models.CharField(max_length=200,
                                   help_text="Descripcion de Evaluacion",
                                   verbose_name="Descripcion")
    
    porcentaje = models.IntegerField(choices=SCORE_CHOICES, blank=True);
    
    id_relacion_curso = models.ForeignKey(RelacionCursoProfesor,
                                          null=False,blank=False,on_delete=models.CASCADE)