from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from phone_field import PhoneField
from django.contrib.auth.models import User
from datetime import date
from django.utils.translation import gettext_lazy as _

# Create your models here.


def validar_edad(fecha_nacimiento):
    fecha_actual = date.today()
    anio_actual = fecha_actual.year
    anio_nacimiento = fecha_nacimiento.year

    edad = anio_actual - anio_nacimiento

    if 16 <= edad <= 150:
        return edad
    else:
        raise ValidationError("Digite una fecha de nacimiento valida")


class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'genero'

    def __str__(self):
        return self.genero

class tipo_Estadocivil(models.Model):
    id_tipoEstadocivil = models.AutoField(primary_key=True)
    nombre_tipoEstadocivil = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'tipo_estadocivil'

    def __str__(self):
        return self.nombre_tipoEstadocivil

class TipoIdentificacion(models.Model):
    id_tipoIdentificacion = models.AutoField(primary_key=True)
    nombreTipoIdentificacion = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'tipo_identificacion'

    def __str__(self):
        return self.nombreTipoIdentificacion


class estado_civil(models.Model):
    id_estadocivil = models.AutoField(primary_key=True, verbose_name="ID Estado Civil")
    id_tipoEstadocivil = models.ForeignKey(tipo_Estadocivil, verbose_name="Estado civil", on_delete=models.PROTECT, null=False, blank=False,default=1)
    nombres_conyugue = models.CharField(max_length=30, null=True, blank=False)
    apellidos_conyugue = models.CharField(max_length=30, null=True, blank=False)
    telefono = PhoneField(max_length=13, null=True, blank=False)

    class Meta:
        db_table = 'estado_civil'
        ordering = ["id_estadocivil"]

    def __str__(self):
        return self.id_tipoEstadocivil.__str__() + " - " + self.nombres_conyugue


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name="Cliente ID")
    id_estadocivil = models.ForeignKey(estado_civil, on_delete=models.PROTECT, null=True)
    nombres = models.CharField(max_length=30, null=False, blank=False)
    apellidos = models.CharField(max_length=30, null=False, blank=False)
    id_genero = models.ForeignKey(Genero, verbose_name="Genero", on_delete=models.PROTECT, null=False, blank=False,default=1)
    id_tipoIdentificacion = models.ForeignKey(TipoIdentificacion, verbose_name="Tipo de identificacion", on_delete=models.PROTECT, null=False, blank=False,default=1)
    identificacion = models.CharField("N° de identificacion", max_length=20, null=False, blank=False)
    fecha_nacimiento = models.DateField("Fecha de nacimiento",null=False, blank=False, help_text="Consejo: <em>Presione en el calendario</em>.", validators=[validar_edad])
    telefono = PhoneField(max_length=13, null=False, blank=False)
    correo = models.EmailField(max_length=35,  null=False, blank=False)
    fotografia = models.ImageField(upload_to='fotografias/', null=True, blank=True)
    es_asociado = models.BooleanField("Es asociado?", null=False, default=False)


    class Meta:
        db_table = 'cliente'
        ordering = ["id_cliente"]

    def __str__(self):
        return self.id_cliente.__str__() + " - " + self.nombres + " - " + self.apellidos + " - " + self.identificacion


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True, verbose_name="Solicitud ID")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_resolocion = models.DateField(null=False, default="1000-01-01")
    es_aprobado = models.BooleanField("Es aprobado?", null=False, default=False)

    class Meta:
        db_table = 'solicitud'
        ordering = ["id_solicitud"]

    def __str__(self):
        return self.id_solicitud + " - " + self.fecha_solicitud + " - " + self.id_cliente.__str__()


class Ubicacioneografica(models.Model):
    id_ubicacion = models.AutoField(primary_key=True, verbose_name="Ubicacion ID")
    direccion = models.CharField(max_length=50, null=False, blank=False)
    latitud = models.FloatField(null=False, blank=False)
    longitud = models.FloatField(null=False, blank=False)

    class Meta:
        db_table = 'ubicacion_google'
        ordering = ["id_ubicacion"]

    def __str__(self):
        return self.id_ubicacion + " - " + self.direccion