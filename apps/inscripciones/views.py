from django.urls import reverse_lazy
from apps.inscripciones.models import Inscripcion
from .form import InscripcionForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class InscripcionListView(ListView):
    model = Inscripcion
    template_name = "inscripcion_list.html"


class InscripcionCreateView(CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'inscripciones/_update_form.html'
    success_url = reverse_lazy('inscripciones')


class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = 'inscripciones/_update_form.html'
    success_url = reverse_lazy('inscripciones')


class InscripcionDeleteView(DeleteView):
    model = Inscripcion
    template_name = "inscripciones/delete.html"
    success_url = reverse_lazy('inscripciones')
