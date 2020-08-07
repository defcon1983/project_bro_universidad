from django import forms
from apps.inscripciones.models import Inscripcion


class InscripcionForm(forms.ModelForm):

	class Meta:

		model = Inscripcion

		fields = '__all__'

		labels = {'id': 'Matricula',
		'fecha': 'Fecha',
		'id_alumno': 'mtrAlumnpo',
		'id_relacion': 'Curso', }

		widgets = {'id': forms.TextInput(attrs={'class': 'form-control'}),
    	'fecha': forms.TextInput(attrs={'class': 'form-control'}),
        'id_alumno': forms.TextInput(attrs={'class': 'form-control'}),
        'id_relacion': forms.TextInput(attrs={'class': 'form-control'}),}
