from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from phone_field import PhoneField
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.


def validar_edad(edad):
    fecha_actual = datetime.now()
    año_actual = fecha_actual.year
    max_edad = año_actual - 16
    min_edad = año_actual - 150

    if True:
        return edad
    else:
        raise ValidationError("Digite una fecha de nacimiento valida")


class Genero(models.Model):
    id_genero = models.AutoField("Cliente ID", primary_key=True)
    genero = models.CharField(max_length=20, null=False, blank=False)


    class Meta:
        db_table = 'genero'

    def __str__(self):
        return self.genero


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name="Cliente ID")
    id_genero = models.ForeignKey(Genero, verbose_name="Genero", on_delete=models.PROTECT, null=False, blank=False, default=1)
    nombres = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    identificacion = models.CharField(max_length=50, null=False, blank=False)
    googleMap = models.CharField("Api Google Maps", max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField("Fecha de nacimiento",null=False, blank=False, help_text="Usar el formato: <em>YYYY-MM-DD</em>.", validators =[validar_edad])
    localidad = models.CharField("Barrio, Colonia etc.", max_length=50, null=False, blank=False)
    telefono = PhoneField(null=False, blank=False)
    correo = models.EmailField(max_length=50,  null=False, blank=False)
    fotografia = models.ImageField(upload_to='fotografias/', null=True, blank=True)

    class Meta:
        db_table = 'cliente'
        ordering = ["id_cliente"]

    def __str__(self):
        return self.identificacion + " - " + self.id_genero.__str__()