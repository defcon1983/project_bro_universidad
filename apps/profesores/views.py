from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.profesores.form import ProfesoresForm
from apps.profesores.models import Profesor

# Create your views here.
def index_profesor(request):
	profesor = Profesor.objects.all().order_by('id')
	contexto = {'profesores':profesor }
	return render(request, 'profesores/index.html', contexto)

def nuevo_profesor(request):
    if request.method == "POST":
        form = ProfesoresForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('index_profesor')
    
    else:
        form = ProfesoresForm()
    
    return render(request, 'profesores/profesores_form.html',{'form':form})

def editar_profesor(request,id_profesor):
	profesor = Profesor.objects.get(id=id_profesor)
	if request.method == "GET":
		form = ProfesoresForm(instance=profesor)
	else:
		form = ProfesoresForm(request.POST,instance=profesor)

		if form.is_valid():
			form.save()

		return redirect('index_profesor')
	return render(request, 'profesores/profesores_form.html',{'form':form})
	return redirect('index_profesor')

def eliminar_profesor(request,id_profesor):
	profesor = Profesor.objects.get(id=id_profesor)
	if request.method == "GET":
		profesor.delete()

		return redirect('index_profesor')
	return render(request, 'profesores/profesores_eliminar.html',{'profesor':profesor})