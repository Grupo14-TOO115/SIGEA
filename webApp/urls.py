from django.urls import path

import cliente.views
from .views import *

# enlaces para mostrar las vistas (URLS)
# path(para pasar parametros, llamado a las  views, nombre de la url)

urlpatterns = [
    path('', home, name='home'),

    path('secretaria', vista_secretaria, name='vista_secretaria'),
    path('secretaria/documentos_anexos', documentos_anexos, name='documentos_anexos'),

    path('jefatura', vista_jefatura, name='vista_jefatura'),

    path('cajera', vista_cajera, name='vista_cajera'),

    path('agente', vista_agente, name='vista_agente'),

    path('asociado', vista_asociado, name='vista_asociado'),

    path('recepcion_solicitudes', solicitudes, name='recepcion_solicitudes'),
    path('solicitudes_espera', solicitudes_espera, name='solicitudes_espera'),
    path('recepcion_solicitudes_validadas', solicitudes_validadas, name='recepcion_solicitudes_validadas'),

    path('ver_solicitud/<int:id_solicitud>', solicitud, name='ver_solicitud'),

    path('solicitud-revisada/<int:id_solicitud>', revisado, name='solicitud-revisada'),
    path('solicitud-validada/<int:id_solicitud>', validado, name='solicitud-validada'),
    path('solicitud-Validada/<int:id_solicitud>', validado2, name='solicitud-Validada'),
    path('solicitud-aprobada/<int:id_solicitud>', aprobado, name='solicitud-validada'),
    path('solicitud-rechazada/<int:id_solicitud>', rechazado, name='solicitud-rechazada'),
]
