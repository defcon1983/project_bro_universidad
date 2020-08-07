from django.conf.urls import url,include
from apps.inscripciones.views import index_inscripciones

urlpatterns = [
    url(r'^$', index_inscripciones,name="index_inscripciones"),
]