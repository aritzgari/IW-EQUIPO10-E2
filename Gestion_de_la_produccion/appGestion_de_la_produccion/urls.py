from django.urls import path
from . import views

urlpatterns = [
    path ('',views.login, name='login'),
    path ('responsable/',views.responsable, name='responsable'),
    path ('responsable/equipo/',views.lista_equipos, name='lista_equipos'),
    path ('responsable/empleado/',views.lista_empleados, name='lista_empleados'),
    path ('responsable/proceso/',views.lista_procesos, name='lista_procesos'),
    path('responsable/equipo/delete', views.eliminarequipo, name='eliminarequipo'),
    path('responsable/empleado/delete', views.eliminarempleado, name='eliminarempleado'),
    path('responsable/proceso/delete', views.eliminarproceso, name='eliminarproceso'),
    path('responsable/equipo/update', views.updateequipo, name='updateequipo'),
    path('responsable/empleado/update', views.updateempleado, name='updateempleado'),
    path('responsable/proceso/update', views.updateproceso, name='updateproceso'),
    path ('responsable/empleado/<int:empleado_id>', views.detalle_empleado, name="detalleempleado"),
    path ('responsable/equipo/<int:equipo_id>', views.detalle_equipo, name="detalleequipo"),
    path ('responsable/proceso/<int:proceso_id>', views.detalle_proceso, name="detalleproceso"),
    path ('operario/proceso/<int:proceso_id>', views.detalle_procesooperario, name="detalleprocesooperario"),
    path ('operario/',views.operario, name='operario'),
    path ('responsable/empleadoform/',views.show_empleado_form, name='empleadoform'),
    path ('responsable/post_empleado/',views.post_empleado_form, name='postempleadoform'),
    path ('responsable/equipoform/',views.show_equipo_form, name='equipoform'),
    path ('responsable/post_equipo/',views.post_equipo_form, name='postequipoform'),
    path ('responsable/procesoform/',views.show_proceso_form, name='procesoform'),
    path ('responsable/post_proceso/',views.post_proceso_form, name='postprocesoform'),
    path ('responsable/guardadocorrectamente/',views.guardadocorrectamente, name='guardadocorrectamente'),

]