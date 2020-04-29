from django.http import HttpResponse
from django.shortcuts import render

from .forms import empleadoform, equipoform, procesoform
from .models import Equipo, Empleado, Proceso

#login

def login(request):
    return render(request,"Login.html")

#Esto nos aporta la lista de equipos
def lista_equipos(request):
    equipo = Equipo.objects.order_by("id")
    context = {"lista_equipos": equipo}
    return render(request, "Equipo.html", context)

def lista_empleados(request):
    empleado = Empleado.objects.order_by("nombre")
    context = {"lista_empleados": empleado}
    return render(request, "Empleado.html", context)

def lista_procesos(request):
    proceso = Proceso.objects.order_by("nombre_proceso")
    context = {"lista_procesos": proceso}
    return render(request, "Proceso.html", context)

#work in progress
def detalle_empleado(request, empleado_id):
    empleado= Empleado.objects.get(pk=empleado_id)
    context={"Datos":empleado}
    return render(request, "detalleempleado.html", context)

def detalle_equipo(request, equipo_id):
    equipo= Equipo.objects.get(pk=equipo_id)
    context={"Datos":equipo}
    return render(request, "detalleequipo.html", context)

def detalle_proceso(request, proceso_id):
    proceso= Proceso.objects.get(pk=proceso_id)
    context={"Datos":proceso}
    return render(request, "detalleproceso.html", context)

def detalle_procesooperario(request, proceso_id):
    proceso= Proceso.objects.get(pk=proceso_id)
    context={"Datos":proceso}
    return render(request, "detalleprocesooperario.html", context)



def responsable(request):
    equipo = Equipo.objects.order_by("modelo")
    empleado = Empleado.objects.order_by("nombre")
    proceso = Proceso.objects.order_by("nombre_proceso")
    context = {"lista_equipos": equipo, "lista_empleados": empleado, "lista_procesos": proceso}
    return render(request, "Responsable.html", context)

def operario(request):
    proceso = Proceso.objects.order_by("nombre_proceso")
    context = {"lista_procesos": proceso}
    return render(request, "Operario.html", context)

def formularioempleado(request):
    return render(request, "FormularioEmpleado.html")

def post_formularioempleado(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    DNI = request.POST["DNI"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    empleado = Empleado(nombre=nombre, apellido=apellido, DNI=DNI, telefono=telefono, email=email, responsable=False)
    empleado.save()
    return render(request, "Guardadocorrectamente.html")

def formularioequipo(request):
    return render(request, "FormularioEquipo.html")

def post_formularioequipo(request):
    marca = request.POST["marca"]
    modelo = request.POST["modelo"]
    categoria = request.POST["categoria"]
    fecha_adquisicion = request.POST["fecha_adquisicion"]
    fecha_instalacion = request.POST["fecha_instalacion"]
    equipo = Equipo(marca=marca, modelo=modelo, categoria=categoria, fecha_adquisicion=fecha_adquisicion,
                    fecha_instalacion=fecha_instalacion)
    equipo.save()
    return render(request, "Guardadocorrectamente.html")

def guardadocorrectamente(request):
    return render(request, "Guardadocorrectamente.html")

def show_empleado_form(request):
    form = empleadoform()
    return render(request, "empleado_form.html", {"form": form})

def post_empleado_form(request):
    form = empleadoform(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellido"]
        DNI = form.cleaned_data["DNI"]
        email = form.cleaned_data["email"]
        telefono = form.cleaned_data["telefono"]
        empleado = Empleado(nombre=nombre, apellido=apellido, DNI=DNI, telefono=telefono, email=email,
                            responsable=False)
        empleado.save()
        return render(request, "Guardadocorrectamente.html")

def show_equipo_form(request):
    form = equipoform()
    return render(request, "equipo_form.html", {"form": form})

def post_equipo_form(request):
    form = equipoform(request.POST)
    if form.is_valid():
        marca = form.cleaned_data["marca"]
        modelo = form.cleaned_data["modelo"]
        categoria = form.cleaned_data["categoria"]
        fecha_adquisicion = form.cleaned_data["fecha_adquisicion"]
        fecha_instalacion = form.cleaned_data["fecha_instalacion"]
        equipo = Equipo(marca=marca, modelo=modelo, categoria=categoria, fecha_adquisicion=fecha_adquisicion,
                        fecha_instalacion=fecha_instalacion)
        equipo.save()
        return render(request, "Guardadocorrectamente.html")

def show_proceso_form(request):
    form = procesoform()
    return render(request, "proceso_form.html", {"form": form})

def post_proceso_form(request):
    form = procesoform(request.POST)

    if form.is_valid():
        form.save()
        return render(request, "Guardadocorrectamente.html")
