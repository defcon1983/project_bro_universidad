from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.cursos.form import CursoForm
from apps.cursos.models import Curso,RelacionCursoProfesor


# Create your views here.
def index_cursos(request):
    curso = Curso.objects.all().order_by('id')
    contexto = {'cursos':curso }
    return render(request, 'cursos/index.html', contexto)

def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('index_cursos')
    
    else:
        form = CursoForm()
    
    return render(request, 'cursos/cursos_form.html',{'form':form})

def editar_curso(request,id_curso):
	curso = Curso.objects.get(id=id_curso)
	if request.method == "GET":
		form = CursoForm(instance=curso)
	else:
		form = CursoForm(request.POST,instance=curso)

		if form.is_valid():
			form.save()

		return redirect('index_cursos')
	return render(request, 'cursos/cursos_form.html',{'form':form})

def eliminar_curso(request,id_curso):
	curso = Curso.objects.get(id=id_curso)
	if request.method == "GET":
		curso.delete()

		return redirect('index_cursos')
	return render(request, 'cursos/cursos_eliminar.html',{'cursos':curso})