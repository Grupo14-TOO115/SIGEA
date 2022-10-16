from django.contrib import admin
from .models import *

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("identificacion","apellidos")
    list_filter = ("id_cliente",)
    search_fields = ("id_cliente","nombres")


admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Genero)
