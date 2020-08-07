from apps.inscripciones.views import InscripcionListView, InscripcionCreateView, InscripcionUpdateView, InscripcionDeleteView
from django.urls import path

urlpatterns = [
    
    path('', InscripcionListView.as_view(), name='inscripciones'),
    path('create/', InscripcionCreateView.as_view(), name = 'crear_inscripcion'),
    path('update/<int:pk>/', InscripcionUpdateView.as_view(), name = 'editar_inscripcion'),
    path('delete/<int:pk>/', InscripcionDeleteView.as_view(), name = 'eliminar_inscripcion'),
]
