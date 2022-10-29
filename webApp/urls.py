from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views
from django.urls import path, include

# enlaces para mostrar las vistas (URLS)
# path(para pasar parametros, llamado a las  views, nombre de la url)

urlpatterns = [
    path('', home, name='home'),
    path('recepcion_solicitudes', views.solicitudes, name='recepcion_solicitudes'),
    path('recepcion_solicitudes_revisadas', views.solicitudes_revisadas, name='recepcion_solicitudes_revisadas'),
    path('ver_solicitud/<int:id_solicitud>/', views.solicitud, name='ver_solicitud'),
]
