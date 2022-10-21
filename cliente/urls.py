from django.urls import path
from .views import *

# enlaces para mostrar las vistas (URLS)

urlpatterns = [
    path('clientes', clientes, name='clientes'),
    path('crear', crear_cliente, name='crear_cliente'),

    path('estado_civil/<int:id_cliente>', crear_estadocivil, name='estado_civil'),
]
