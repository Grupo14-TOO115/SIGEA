from django.urls import path
from .views import *

# enlaces para mostrar las vistas (URLS)

urlpatterns = [
    path('clientes', clientes, name='clientes'),
    path('crear', crear_cliente, name='crear_cliente'),
    path('crearActividad/<int:id_solicitud>', crear_actividad_economica, name='crear_actividad_economica'),
    path('crearCapacidadEconomica/<int:id_solicitud>/<int:id_actividadEconomica>',crear_capacidad_economica, name='crear_capacidad_economica'),
    path('localidad/<int:id_cliente>', localidad, name='localidad'),
    path('estado_civil/<int:id_cliente>', crear_estadocivil, name='estado_civil'),
]
