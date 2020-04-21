from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name ="index"),
    path ('equipo/<int:equipo_id>', views.detailEquipo, name="detailEquipo"),
    path ('empleado/<int:empleado_id>', views.detailEmpleado, name="detailEmpleado"),
    path ('proceso/<int:proceso_id>', views.detailProceso, name="detailProceso")
]