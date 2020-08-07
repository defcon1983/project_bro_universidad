from django.contrib import admin
from apps.cursos.models import Curso, RelacionCursoProfesor

# Register your models here.
admin.site.register(Curso)
admin.site.register(RelacionCursoProfesor)