from django.db import models

#Modelo del equipo
class Equipo(models.Model):
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    categoria = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    fecha_instalacion = models.DateField()

    def __str__(self):
        return f"id ={self.id}, modelo={self.modelo}, marca={self.marca}, categoria={self.categoria}, fecha_adquisicion={self.fecha_adquisicion}, fecha_instalacion={self.fecha_instalacion}"

#Modelo del empleado
class Empleado(models.Model):

    nombre = models.CharField(max_length=50)
    DNI = models.CharField(max_length=9)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    responsable=models.BooleanField()

    def __str__(self):
        return f"id ={self.id},responsable={self.responsable}, nombre={self.nombre}, apellido={self.apellido}, DNI={self.DNI}, email={self.email}, telefono={self.telefono}"

#Modelo del proceso
class Proceso(models.Model):
    empleados_asignados = models.ManyToManyField(Empleado)
    equipo=models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True)
    codigo_orden = models.CharField(max_length=10)
    codigo_proceso = models.IntegerField()
    nombre_proceso = models.CharField(max_length=50)
    referencia = models.CharField(max_length=10)
    inicio = models.DateField()
    fin = models.DateField()

    def __str__(self):
        return f"codigoorden={self.codigo_orden}, codigo_proceso={self.codigo_proceso}, nombre_proceso={self.nombre_proceso}, referencia={self.referencia}, inicio={self.inicio}, fin={self.fin}"
