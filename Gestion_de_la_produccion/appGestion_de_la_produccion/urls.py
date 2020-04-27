from django.urls import path
from . import views

urlpatterns = [
    path ('',views.login, name='login'),
    path ('responsable/equipo/',views.lista_equipos, name='lista_equipos'),
    path ('responsable/empleado/',views.lista_empleados, name='lista_empleados'),
    path ('responsable/proceso/',views.lista_procesos, name='lista_procesos'),
    path ('responsable/',views.responsable, name='responsable'),
    path ('operario/',views.operario, name='operario'),
    path ('responsable/formularioempleado/',views.formularioempleado, name='formularioempleado'),
    path ('registrarempleados/',views.post_formularioempleado, name='postformularioempleado'),
    path ('responsable/formularioequipo/',views.formularioequipo, name='formularioequipo'),
    path ('registrarequipo/',views.post_formularioequipo, name='postformularioequipo'),
    path ('responsable/empleadoform/',views.show_empleado_form, name='empleadoform'),
    path ('responsable/post_empleado/',views.post_empleado_form, name='postempleadoform'),

]