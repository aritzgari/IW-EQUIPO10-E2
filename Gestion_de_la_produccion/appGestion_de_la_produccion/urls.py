from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Url inicial.
    path('', views.get_login, name='get_login'),
    # Url intermediaria para redirigirte a la página principal de responsable o de operario.
    path('index/', views.index, name='index'),
    # Url para registrar los nuevos usuarios.
    path('register/', views.register, name='do_register'),
    # Url que se encarga de comparar lo introducido en los campos del login con lo que hay dentro de la BD.
    path('dologin/', views.do_login, name='do_login'),
    # Url de inicio en la que podemos elegir entre ser un operario o un responsable.
    path('responsable/', views.responsable, name='responsable'),  # Url de inicio de responsable
    path('responsable/equipo/', views.lista_equipos, name='lista_equipos'),  # Url que da la lista de todos los equipos
    path('responsable/empleado/', views.lista_empleados, name='lista_empleados'),
    # Url que da la lista de todos los empleados
    path('responsable/proceso/', views.lista_procesos, name='lista_procesos'),
    # Url que da la lista de todos los procesos
    path('responsable/equipo/delete', views.eliminarequipo, name='eliminarequipo'),  # Url para eliminar equipos
    path('responsable/empleado/delete', views.eliminarempleado, name='eliminarempleado'),  # Url para eliminar empleados
    path('responsable/proceso/delete', views.eliminarproceso, name='eliminarproceso'),  # Url para eliminar procesos
    path('responsable/equipo/update', views.updateequipo, name='updateequipo'),  # Url para updatear equipos
    path('responsable/empleado/update', views.updateempleado, name='updateempleado'),  # Url para updatear empleados
    path('responsable/proceso/update', views.updateproceso, name='updateproceso'),  # Url para updatear procesos
    path('responsable/empleado/<int:empleado_id>', views.detalle_empleado, name="detalleempleado"),
    # Url de detalles de empleados, desde aqui se puede ir a eliminar y updatear
    path('responsable/equipo/<int:equipo_id>', views.detalle_equipo, name="detalleequipo"),
    # Url de detalles de equipo, desde aqui se puede ir a eliminar y updatear
    path('responsable/proceso/<int:proceso_id>', views.detalle_proceso, name="detalleproceso"),
    # Url de detalles de proceso, desde aqui se puede ir a eliminar y updatear
    path('operario/proceso/<int:proceso_id>', views.detalle_procesooperario, name="detalleprocesooperario"),
    # Url de detalles de proceso, se puede ir a modificar inicio y fin
    path('operario/proceso/update', views.updateprocesooperario, name='updateprocesooperario'),
    # Url para updatear procesos desde los privilegios de un operario
    path('operario/post_proceso_update_operario/', views.post_proceso_form_update_operario,
         name='postprocesoformupdateoperario'),
    # Url para envio de los datos de los formularios de update desde los privilegios de un operario
    path('operario/', views.operario, name='operario'),  # Url inicial de operarios
    path('responsable/empleadoform/', views.show_empleado_form, name='empleadoform'),
    # Url para visualizar el formulario de introducir empleados.
    path('responsable/post_empleado/', views.post_empleado_form, name='postempleadoform'),
    # Url para enviar los datos del formulario de empleados a BD.
    path('responsable/equipoform/', views.show_equipo_form, name='equipoform'),
    # Url para visualizar el formulario de introducir equipos.
    path('responsable/post_equipo/', views.post_equipo_form, name='postequipoform'),
    # Url para enviar los datos del formulario de equipos a BD.
    path('responsable/procesoform/', views.show_proceso_form, name='procesoform'),
    # Url para visualizar el formulario de introducir procesos.
    path('responsable/post_proceso/', views.post_proceso_form, name='postprocesoform'),
    # Url para enviar los datos del formulario de procesos a BD.
    path('responsable/post_empleado_update/', views.post_empleado_form_update, name='postempleadoformupdate'),
    # Url para enviar los datos del formulario de empleados a BD y actualizarlos.
    path('responsable/post_equipo_update/', views.post_equipo_form_update, name='postequipoformupdate'),
    # Url para enviar los datos del formulario de equipos a BD y actualizarlos.
    path('responsable/post_proceso_update/', views.post_proceso_form_update, name='postprocesoformupdate'),
    # Url para enviar los datos del formulario de procesos a BD y actualizarlos.
    path('responsable/guardadocorrectamente/', views.guardadocorrectamente, name='guardadocorrectamente'),
    # Si te sale esta página es que se ha guardado correctamente la información en BD.
    path('operario/deleteAPI', views.borrar_proceso_checkbox, name='borraroperario'),
    # Url para dar por finalizado un proceso.
    path('responsable/equipo/añadirequipoAPI', views.anadir_equipo_ayax, name='añadirequipoayax')
    # Url para añadir un equipo mediante el formulario y ajax.
]
