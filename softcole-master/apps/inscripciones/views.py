from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def index_inscripciones(request):
	return render(request, 'inscripciones/index.html')



 # inscriociones es la carpeta y el otro despues de la coma es el archivo html.
