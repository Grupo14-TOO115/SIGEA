from django.urls import path
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
    path('recepcion_solicitudes_revisadas', solicitudes_revisadas, name='recepcion_solicitudes_revisadas'),
    path('ver_solicitud/<int:id_solicitud>', solicitud, name='ver_solicitud'),
]
