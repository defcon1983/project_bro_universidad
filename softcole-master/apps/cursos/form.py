from django import forms
from apps.cursos.models import Curso, RelacionCursoProfesor


class CursoForm(forms.ModelForm):

	class Meta:
		model = Curso
		relacion = RelacionCursoProfesor
		
		fields = ['descripcion']

		labels={'descripcion':'Nombre del Curso',}

		widgets={'descripcion':forms.TextInput(attrs={'class':'form-control'}),}
