from django.conf.urls import url,include
from apps.profesores.views import index_profesor, nuevo_profesor,editar_profesor,eliminar_profesor


urlpatterns = [
    url(r'^$', index_profesor, name='index_profesor'),
    url(r'^nuevo$', nuevo_profesor, name='nuevo_profesor'),
    url(r'^editar/(?P<id_profesor>\d+)/$', editar_profesor, name='editar_profesor'),
    url(r'^eliminar/(?P<id_profesor>\d+)/$', eliminar_profesor, name='eliminar_profesor'),
]
