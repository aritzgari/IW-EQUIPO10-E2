from django.db import models


# Create your models here.



class Equipo(models.Model):
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    categoria = models.CharField(max_length=50)
    fecha_adquision = models.DateField()
    fecha_instalacion = models.DateField()

    def __str__(self):
        return f"modelo={self.modelo},marca={self.marca}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    DNI = models.CharField(max_length=9)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return f"nombre={self.nombre},apellido={self.apellido},DNI={self.DNI}"


class Proceso(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=callable(Equipo.marca))
    empleados_asignados = models.ManyToManyField(Empleado)
    codigo_orden = models.CharField(max_length=10)
    codigo_proceso = models.IntegerField()
    nombre_proceso = models.CharField(max_length=50)
    referencia = models.CharField(max_length=10)
    inicio = models.DateField()
    fin = models.DateField()


    def __str__(self):
        return f"codigoorden={self.codigoorden},nombreproceso={self.nombreproceso}"
