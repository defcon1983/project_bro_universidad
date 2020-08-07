from django.conf.urls import url,include
from apps.cursos.views import index_cursos,nuevo_curso,editar_curso,eliminar_curso

urlpatterns = [
    url(r'^$', index_cursos,name="index_cursos"),
    url(r'^nuevo$', nuevo_curso, name='nuevo_curso'),
    url(r'^editar/(?P<id_curso>\d+)/$', editar_curso, name='editar_curso'),
    url(r'^eliminar/(?P<id_curso>\d+)/$', eliminar_curso, name='eliminar_curso'),
]
