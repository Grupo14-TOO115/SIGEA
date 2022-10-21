from django.urls import path
from .views import *

# enlaces para mostrar las vistas (URLS)
# path(para pasar parametros, llamado a las  views, nombre de la url)

urlpatterns = [
    path('', home, name='home'),
    path('secretaria/documentos_anexos', documentos_anexos, name='documentos_anexos'),
]
