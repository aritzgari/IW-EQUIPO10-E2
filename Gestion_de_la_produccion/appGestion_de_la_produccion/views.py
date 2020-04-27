from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo, Empleado, Proceso
from .forms import empleadoform

def login(request):

    return render(request,"Login.html")

def lista_equipos(request):
    equipo = Equipo.objects.order_by("modelo")
    context = {"lista_equipos": equipo}
    return render(request,"Equipo.html",context)

def lista_empleados(request):
    empleado=Empleado.objects.order_by("nombre")
    context = {"lista_empleados": empleado}
    return render(request,"Empleado.html",context)

def lista_procesos(request):
    proceso=Proceso.objects.order_by("nombre_proceso")
    context = {"lista_procesos": proceso}
    return render(request,"Proceso.html",context)
def responsable(request):
    equipo = Equipo.objects.order_by("modelo")
    empleado=Empleado.objects.order_by("nombre")
    proceso=Proceso.objects.order_by("nombre_proceso")
    context={"lista_equipos": equipo,"lista_empleados": empleado, "lista_procesos": proceso}
    return render(request,"Responsable.html", context)

def operario(request):
    proceso=Proceso.objects.order_by("nombre_proceso")
    context = {"lista_procesos": proceso}
    return render(request,"Operario.html",context)

def formularioempleado(request):
    return render(request,"FormularioEmpleado.html")

def post_formularioempleado(request):
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    DNI=request.POST["DNI"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]

    return HttpResponse("El empleado se ha guardado correctamente")

def formularioequipo(request):
    return render(request,"FormularioEquipo.html")

def post_formularioequipo(request):
    marca=request.POST["marca"]
    modelo=request.POST["modelo"]
    categoria=request.POST["categoria"]
    fecha_adquisicion = request.POST["fecha_adquisicion"]
    fecha_instalacion = request.POST["fecha_instalacion"]

    return HttpResponse("El equipo se ha guardado correctamente")

def show_empleado_form(request):
    form= empleadoform()
    return render(request,"empleado_form.html",{"form":form})
def post_empleado_form(request):
    form=empleadoform(request.POST)
    if form.is_valid():
        nombre=form.cleaned_data["nombre"]
        apellido=form.cleaned_data["apellido"]
        DNI=form.cleaned_data["DNI"]
        return HttpResponse(f"El usuario {nombre} {apellido} con DNI {DNI} ha sido guardado correctamente")