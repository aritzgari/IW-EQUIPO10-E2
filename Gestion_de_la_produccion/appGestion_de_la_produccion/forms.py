from django import forms
from django.forms import DateInput

from .models import Empleado, Equipo, Proceso


class empleadoform(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.CharField(label="Email", max_length=150)
    DNI = forms.CharField(label="DNI", max_length=9)
    telefono = forms.IntegerField(label="Telefono")


class equipoform(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50)
    modelo = forms.CharField(label="Modelo", max_length=50)
    categoria = forms.CharField(label="Categoria", max_length=50)
    fecha_adquisicion = forms.DateField(label="Fecha de adquisicion",
                                        widget=forms.SelectDateWidget(years=range(1970, 2050)))
    fecha_instalacion = forms.DateField(label="Fecha de instalacion",
                                        widget=forms.SelectDateWidget(years=range(1970, 2050)))


class procesoform(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ('__all__')
        widgets = {
            'inicio': forms.SelectDateWidget(years=range(1970, 2050)),
            'fin': forms.SelectDateWidget(years=range(1970, 2050)),
        }


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)



class LoginForm(forms.Form):
    # Usuario
    usuario = forms.CharField(max_length=100)

    # Contraseña
    attrs = {
        "type": "password"  # Atributo para mostrarlo como contraseña
    }
    contrasena = forms.CharField(widget=forms.TextInput(attrs=attrs))
