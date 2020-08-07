from django import forms
from apps.alumnos.models import Alumno

class AlumnosForm(forms.ModelForm):

	class Meta:
		model = Alumno
		fields = ['rut','rut','nombres','telefono','correo',
				  'fecha_nacimiento','sexo','tipo_sangre',
				  'domicilio','nombres','telefono','correo',
				  'fecha_nacimiento','sexo','tipo_sangre','domicilio']
		labels = {'rut':'Id',
				  'nombres':'Nombres y Apellidos',
				  'telefono':'Telefono Movil',
				  'correo':'Correo electronico',
				  'fecha_nacimiento':'Fecha de Nacimiento',
				  'sexo':'Sexo',
				  'tipo_sangre':'Tipo de Sangre',
				  'domicilio':'Domicilio',}
		widgets = {'rut':forms.TextInput(attrs={'class':'form-control'}),
				   'nombres':forms.TextInput(attrs={'class':'form-control'}),
				   'telefono':forms.TextInput(attrs={'class':'form-control'}),
				   'correo':forms.EmailInput(attrs={'class':'form-control'}),
				   'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control'}),
				   'sexo':forms.Select(attrs={'class':'form-control'}),
				   'tipo_sangre':forms.TextInput(attrs={'class':'form-control'}),
				   'domicilio':forms.Textarea(attrs={'class':'form-control'}),}