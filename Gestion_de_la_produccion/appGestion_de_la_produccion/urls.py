from django.urls import path
from . import views

urlpatterns = [
    #path ('',views.login, name='login'),
    path ('responsable/equipo/',views.lista_equipos, name='lista_equipos'),
    path ('responsable/empleado/',views.lista_empleados, name='lista_empleados'),
    path ('responsable/proceso/',views.lista_procesos, name='lista_procesos'),
    path ('responsable/',views.responsable, name='responsable'),
    path ('empleado/<int:empleado_id>', views.detalle_empleado, name="detalleempleado"),
    path ('operario/',views.operario, name='operario'),
    path ('responsable/empleadoform/',views.show_empleado_form, name='empleadoform'),
    path ('responsable/post_empleado/',views.post_empleado_form, name='postempleadoform'),
    path ('responsable/equipoform/',views.show_equipo_form, name='equipoform'),
    path ('responsable/post_equipo/',views.post_equipo_form, name='postequipoform'),
    path ('responsable/procesoform/',views.show_proceso_form, name='procesoform'),
    path ('responsable/post_proceso/',views.post_proceso_form, name='postprocesoform'),
    path ('responsable/guardadocorrectamente/',views.guardadocorrectamente, name='guardadocorrectamente'),

]