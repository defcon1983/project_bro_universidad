from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.alumnos.form import AlumnosForm
from apps.alumnos.models import Alumno

# Create your views here.
def index_alumnos(request):
	alumno = Alumno.objects.all().order_by('id')
	contexto = {'alumnos':alumno }
	return render(request, 'alumnos/index.html', contexto)

def nuevo_alumno(request):
    if request.method == "POST":
        form = AlumnosForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('index_alumnos')
    
    else:
        form = AlumnosForm()
    
    return render(request, 'alumnos/alumnos_form.html',{'form':form})

def editar_alumno(request,id_alumno):
	alumno = Alumno.objects.get(id=id_alumno)
	if request.method == "GET":
		form = AlumnosForm(instance=alumno)
	else:
		form = AlumnosForm(request.POST,instance=alumno)

		if form.is_valid():
			form.save()

		return redirect('index_alumnos')
	return render(request, 'alumnos/alumnos_form.html',{'form':form})	

def eliminar_alumno(request,id_alumno):
	editar_alumno = Alumno.objects.get(id=id_alumno)
	if request.method == "GET":
		alumno.delete()

		return redirect('index_alumnos')
	return render(request, 'alumnos/alumnos_eliminar.html',{'alumnos':alumno})