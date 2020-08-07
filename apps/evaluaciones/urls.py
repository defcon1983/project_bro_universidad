from django.conf.urls import url,include
from apps.evaluaciones.views import index_evaluaciones

urlpatterns = [
    url(r'^$', index_evaluaciones,name="admin_evaluaciones"),
]