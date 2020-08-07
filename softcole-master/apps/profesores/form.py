from django import forms
from apps.profesores.models import Profesor 

class ProfesoresForm(forms.ModelForm):
    
    class Meta:
        model = Profesor
        
        fields = [
                 'rut',
                 'nombre',
                 'telefono',
                 'correo',
                 'fecha_nacimiento',
                 'sexo',
                 'tipo_sangre',
                 'domicilio',
            ] 
        labels = {
                'rut':'ID',
                 'nombre':'Nombres y Apellidos',
                 'telefono':'Telefono Movil',
                 'correo':'Correo electronico',
                 'fecha_nacimiento':'Fecha de Nacimiento',
                 'sexo':'Sexo',
                 'tipo_sangre':'Tipo de Sangre',
                 'domicilio':'Domicilio',
            }
        widgets={
                'rut':forms.TextInput(attrs={'class':'form-control'}),
                 'nombres':forms.TextInput(attrs={'class':'form-control'}),
                 'telefono':forms.TextInput(attrs={'class':'form-control'}),
                 'correo':forms.EmailInput(attrs={'class':'form-control'}),
                 'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control'}),
                 'sexo':forms.Select(attrs={'class':'form-control'}),
                 'tipo_sangre':forms.TextInput(attrs={'class':'form-control'}),
                 'domicilio':forms.Textarea(attrs={'class':'form-control'}),
            }