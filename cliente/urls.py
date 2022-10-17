from django.urls import path
from .views import *

# enlaces para mostrar las vistas (URLS)

urlpatterns = [
    path('clientes', clientes, name='clientes'),
    path('crear', crear_cliente, name='crear_cliente'),
]
