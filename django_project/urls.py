"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls')),
    path('', include('webApp.urls')),
    path('cliente/', include('cliente.urls')),
    path('jefatura/', include('jefatura.urls')),
    path('secretaria/', include('secretaria.urls')),
    path('agente/', include('agente.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('cajero/', include('cajero.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'autenticacion.views.error_404'
handler500 = 'autenticacion.views.error_500'
handler403 = 'autenticacion.views.error_403'
handler400 = 'autenticacion.views.error_400'
