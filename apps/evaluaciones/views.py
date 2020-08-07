from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_evaluaciones(request):
    return render(request, 'academicos/admin_evaluaciones.html');

