from django.http import HttpResponse
from django.shortcuts import render, redirect

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

#Esto nos aporta la lista de empleados
def lista_empleados(request):
    empleado = Empleado.objects.order_by("nombre")
    context = {"lista_empleados": empleado}
    return render(request, "Empleado.html", context)

#Esto nos aporta la lista de procesos
def lista_procesos(request):
    proceso = Proceso.objects.order_by("nombre_proceso")
    context = {"lista_procesos": proceso}
    return render(request, "Proceso.html", context)

#Detalles del empleado
def detalle_empleado(request, empleado_id):
    empleado= Empleado.objects.get(pk=empleado_id)
    context={"Datos":empleado}
    return render(request, "detalleempleado.html", context)

#Detalles del equipo
def detalle_equipo(request, equipo_id):
    equipo= Equipo.objects.get(pk=equipo_id)
    context={"Datos":equipo}
    return render(request, "detalleequipo.html", context)

#Detalles del proceso
def detalle_proceso(request, proceso_id):
    proceso= Proceso.objects.get(pk=proceso_id)
    context={"Datos":proceso}
    return render(request, "detalleproceso.html", context)

#Detalles del proceso desde el punto de vista del operario
def detalle_procesooperario(request, proceso_id):
    proceso= Proceso.objects.get(pk=proceso_id)
    context={"Datos":proceso}
    return render(request, "detalleprocesooperario.html", context)

#Pagina principal del responsable
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


# Funcion para elimiar el equipo de detalles
def eliminarequipo(req):
    equipoBorrar = Equipo()
    equipoBorrar.id = int(req.POST['idEquipo'])
    equipoBorrar.delete()
    return redirect('lista_equipos')

# Funcion para elimiar el empleado de detalles
def eliminarempleado(req):
    empleadoBorrar = Empleado()
    empleadoBorrar.id = int(req.POST['idEmpleado'])
    empleadoBorrar.delete()
    return redirect('lista_empleados')

# Funcion para elimiar el proceso de detalles
def eliminarproceso(req):
    procesoBorrar = Proceso()
    procesoBorrar.id = int(req.POST['idProceso'])
    procesoBorrar.delete()
    return redirect('lista_procesos')

#Updatear el equipo
def updateequipo(request):
    equipoid = int(request.POST['idEquipo'])
    equipo= Equipo.objects.get(pk=equipoid)
    context={"Datos":equipo}
    return render(request, "updateequipo.html", context)

#Updatear el empleado
def updateempleado(request):
    empleadoid = int(request.POST['idEmpleado'])
    empleado= Empleado.objects.get(pk=empleadoid)
    context={"Datos":empleado}
    return render(request, "updateempleado.html", context)

#Updatear el proceso
def updateproceso(request):
    procesoid = int(request.POST['idProceso'])
    proceso= Proceso.objects.get(pk=procesoid)

    empleado= Empleado.objects.all()
    equipo= Equipo.objects.all()
    context={"Datos":proceso,"Datos2":empleado,"Datos3": equipo}
    return render(request, "updateproceso.html", context)

#Formulario de update de empleados
def post_empleado_form_update(req):
    form = empleadoform(req.POST)
    if form.is_valid():
        empleado = Empleado()
        empleado.id = int(req.POST["empleado_id"])
        empleado.nombre = str(req.POST['nombre'])
        empleado.apellido = str(req.POST['apellido'])
        empleado.DNI = str(req.POST['DNI'])
        empleado.email = str(req.POST['email'])
        empleado.telefono = str(req.POST['telefono'])
        empleado.responsable = bool(req.POST['responsable'])
        empleado.save()
        return render(req, "Guardadocorrectamente.html")

#Formulario de update de empleados
def post_equipo_form_update(req):
        form = equipoform(req.POST)
        if form.is_valid():
            equipo = Equipo()
            equipo.id = int(req.POST["equipo_id"])
            equipo.modelo = str(req.POST['modelo'])
            equipo.marca = str(req.POST['marca'])
            equipo.categoria = str(req.POST['categoria'])
            equipo.fecha_adquisicion = req.POST['fecha_adquisicion']
            equipo.fecha_instalacion = req.POST['fecha_instalacion']
            equipo.save()
            return render(req, "Guardadocorrectamente.html")

#Formulario de update de procesos
def post_proceso_form_update(request):

    form = procesoform(request.POST)

    if form.is_valid():

        procesoupdate = Proceso.objects.get(pk=request.POST["proceso_id"])
        procesoupdate.codigo_orden=str(request.POST["codigo_orden"])
        procesoupdate.codigo_proceso=int(request.POST["codigo_proceso"])
        procesoupdate.nombre_proceso=str(request.POST["nombre_proceso"])
        procesoupdate.referencia=str(request.POST["referencia"])
        procesoupdate.inicio = request.POST['inicio']
        procesoupdate.fin = request.POST['fin']
        procesoupdate.empleados_asignados.set(Empleado.objects.filter(id__in=request.POST.getlist("empleados_asignados")))
        procesoupdate.equipo=(Equipo.objects.get(pk=request.POST["equipo"]))
        procesoupdate.save()
        return render(request, "Guardadocorrectamente.html")

#Updatear el proceso desde operario
def updateprocesooperario(request):
    procesoid = int(request.POST['idProceso'])
    proceso= Proceso.objects.get(pk=procesoid)
    context={"Datos":proceso}
    return render(request, "updateprocesooperario.html", context)

#Formulario de update de procesos desde operario
def post_proceso_form_update_operario(request):
    form = procesoform(request.POST)
    if form.is_valid():
        procesoupdate = Proceso.objects.get(pk=request.POST["idProceso"])
        procesoupdate.inicio = request.POST['inicio']
        procesoupdate.fin = request.POST['fin']
        procesoupdate.save()
        return render(request, "Guardadocorrectamente.html")
