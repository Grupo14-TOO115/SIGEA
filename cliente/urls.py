from django.urls import path
from .views import *
from django.urls import path, include
# enlaces para mostrar las vistas (URLS)

urlpatterns2 = [
    path('crearActividad/', crear_actividad_economica, name='crear_actividad_economica'),
    path('crearCapacidadEconomica', crear_capacidad_economica, name='crear_capacidad_economica'),
    path('localidad/', localidad, name='localidad'),
    path('estado_civil', crear_estadocivil, name='estado_civil'),
]

urlpatterns = [
    path('crear', crear_cliente, name='crear_cliente'),
    path('solicitud/<int:id_solicitud>/', include(urlpatterns2)),
]
