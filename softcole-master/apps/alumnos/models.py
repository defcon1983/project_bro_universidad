from django.db import models
 
# Create your models here.
class Alumno(models.Model):
    GENERO = (('M','Masculino'),('F','Femenino'))
    #campos:
    rut = models.CharField(max_length=13,help_text="Indique su RUT",verbose_name="Id")
    nombres=models.CharField(max_length=100, 
                             help_text="Nombres y Apellidos",
                             verbose_name="Nombres")
    telefono=models.CharField(max_length=100, 
                             help_text="Numero de Telefono. ej: +56555555555",
                             verbose_name="Telefono")
    correo=models.EmailField( help_text="Correo Electronico",
                              verbose_name="Correo Electronico")
    fecha_nacimiento = models.DateField( help_text="Fecha de Nacimiento",
                                         verbose_name="Fec. Nac.")
    sexo = models.CharField(max_length=1,
                            help_text="Masculino o Femenino",
                            verbose_name="Sexo",
                            choices=GENERO)
    tipo_sangre=models.CharField(max_length=5,
                                 help_text="Tipo de Sangre. ej: ORH-",
                                 verbose_name="Tipo de Sangre")
    domicilio=models.TextField(help_text="Direccion de Habitacion",
                             verbose_name="Domicilio",default="")
    fecha = models.DateField(auto_now=True)
    