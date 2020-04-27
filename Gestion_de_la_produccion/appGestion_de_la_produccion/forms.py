from django import forms

class empleadoform(forms.Form):
    nombre= forms.CharField(label="Nombre",max_length=100)
    apellido= forms.CharField(label="Apellido",max_length=100)
    email= forms.CharField(label="Email",max_length=150)
    DNI= forms.CharField(label="DNI",max_length=9)
    telefono= forms.IntegerField(label="Telefono")




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