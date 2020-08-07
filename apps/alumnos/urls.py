from django.conf.urls import url,include
from apps.alumnos.views import index_alumnos,nuevo_alumno,editar_alumno,eliminar_alumno

urlpatterns = [
    url(r'^$', index_alumnos,name="index_alumnos"),
    url(r'^nuevo$', nuevo_alumno, name='nuevo_alumno'),
    url(r'^editar/(?P<id_alumno>\d+)/$', editar_alumno, name='editar_alumno'),
    url(r'^eliminar/(?P<id_alumno>\d+)/$', eliminar_alumno, name='eliminar_alumno'),
]