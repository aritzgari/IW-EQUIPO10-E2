from django import forms

from .models import Empleado, Equipo, Proceso


class empleadoform(forms.Form):
    nombre= forms.CharField(label="Nombre",max_length=100)
    apellido= forms.CharField(label="Apellido",max_length=100)
    email= forms.CharField(label="Email",max_length=150)
    DNI= forms.CharField(label="DNI",max_length=9)
    telefono= forms.IntegerField(label="Telefono")


class equipoform(forms.Form):
    marca= forms.CharField(label="Marca",max_length=50)
    modelo= forms.CharField(label="Modelo",max_length=50)
    categoria= forms.CharField(label="Categoria",max_length=50)
    fecha_adquisicion= forms.DateField(label="Fecha de adquisicion",widget=forms.SelectDateWidget)
    fecha_instalacion= forms.DateField(label="Fecha de instalacion",widget=forms.SelectDateWidget)

class procesoform(forms.ModelForm):
    class Meta:
        model=Proceso
        fields = '__all__'
    # equipolista = Equipo.objects.order_by("modelo")
    # empleado_asignado= forms.MultipleChoiceField(label="Empleado asignados",widget=forms.CheckboxSelectMultiple,choices=empleadolista)
    # equipo= forms.ChoiceField(label="Equipo",widget=forms.CheckboxInput)
    # codigo_orden= forms.CharField(label="Codigo de orden",max_length=10)
    # codigo_proceso= forms.IntegerField(label="Codigo de proceso")
    # nombre_proceso=forms.CharField(label="Nombre del proceso",max_length=50)
    # referencia=forms.CharField(label="Referencia",max_length=10)
    # inicio=forms.DateField(label="Inicio",widget=forms.SelectDateWidget)
    # fin=forms.DateField(label="Fin",widget=forms.SelectDateWidget)


# Formulario crear Empleados
# class EmpleadoForm(forms.ModelForm):
#     class Meta:
#         model=Empleado
#         fields = 'all'


# Formulario crear Equipos
# class EquipoForm(forms.ModelForm):
#     class Meta:
#         model=Equipo
#         fields = 'all'


# Formulario crear Tareas
# class TareaForm(forms.ModelForm):
#     class Meta:
#         model=Tarea
#         fields = 'all'


# Formulario de Registro
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields = ('username','password','email')


# Formulario de Inicio de Sesion
# class LoginForm(forms.Form):
#     # Usuario
#     username=forms.CharField(max_length=100)

    # Contraseña
    # attrs = {
    #     "type": "password" # Atributo para mostrarlo como contraseña
    # }
    # password = forms.CharField(widget=forms.TextInput(attrs=attrs))