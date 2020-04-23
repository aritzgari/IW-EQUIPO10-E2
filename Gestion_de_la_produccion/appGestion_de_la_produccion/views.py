from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo, Empleado, Proceso

def index(request):
    equipo = Equipo.objects.order_by("modelo")
    output = ' , '.join([d.modelo for d in equipo])
    empleado=Empleado.objects.order_by("nombre")
    output2 = ' , '.join([d.nombre for d in empleado])
    proceso=Proceso.objects.order_by("nombre_proceso")
    output3 = ' , '.join([d.nombre_proceso for d in proceso])
    return HttpResponse ("Equipos: "+output+"\n Empleados: "+output2+"\n Procesos: "+output3)

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

def detailEquipo (request, equipo_id):
    equipo=Equipo.objects.get(pk=equipo_id)
    return HttpResponse(equipo)

def detailEmpleado (request, empleado_id):
    empleado=Empleado.objects.get(pk=empleado_id)
    return HttpResponse(empleado)

def detailProceso (request, proceso_id):
    proceso=Proceso.objects.get(pk=proceso_id)
    return HttpResponse(proceso)
