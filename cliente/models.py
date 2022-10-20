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


class TipoIdentificacion(models.Model):
    id_tipoIdentificacion = models.AutoField(primary_key=True)
    nombreTipoIdentificacion = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'tipo_identificacion'

    def __str__(self):
        return self.nombreTipoIdentificacion


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name="Cliente ID")
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
class Profesion(models.Model):
    id_profesion = models.AutoField(primary_key=True, verbose_name="Profesion ID")
    nombre_profesion= models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'profesion'
        ordering = ["id_profesion"]

    def __str__(self):
        return self.nombre_profesion


class CapacidadEconomica(models.Model):
    id_capacidadEconomica = models.AutoField(primary_key=True, verbose_name="Capacidad Economica ID")
    salario = models.DecimalField("Salario", max_digits=8, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosAFP = models.DecimalField("Descuento de AFP", max_digits=8, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosISSS = models.DecimalField("Descuento de ISSS", max_digits=8, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosPersonales = models.DecimalField("Gastos Personales", max_digits=8, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    prestamos = models.DecimalField("Prestamos Bancarios", max_digits=8, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosEducacion = models.DecimalField("Gastos de Educacion", max_digits=8, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    otrosIngresos = models.DecimalField("Otros Ingresos",max_digits=8, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    total = models.DecimalField("Total Capacidad Econoomica", max_digits=8, decimal_places=2)
    class Meta:
        db_table = 'CapacidadEconomica'
        ordering = ["id_capacidadEconomica"]

    def __str__(self):
        return self.id_capacidad + " - " + self.total

class ActividadEconomica(models.Model):
    id_actividadEconomica = models.AutoField(primary_key=True, verbose_name="Actividad Economica ID")
    id_capacidadEconomica = models.ForeignKey(CapacidadEconomica, verbose_name="Capacidad Economica",on_delete=models.PROTECT,null= True)
    id_profesion = models.ForeignKey(Profesion, verbose_name="Profesion",on_delete=models.PROTECT, null=False)
    es_empresario = models.BooleanField("Es asociado?", null=False, default=False)
    lugarTrabajo = models.CharField("Lugar de trabajo",max_length=50, null=False, blank=False)
    telefono = PhoneField("Telefono de lugar de trabajo",max_length=13, null=False, blank=False)
    class Meta:
        db_table = 'ActividadEconomica'


    def __str__(self):
        return self.id_actividadEconomica + " - " + self.id_capacidadEconomica + " - " + self.id_profesion

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True, verbose_name="Solicitud ID")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)
    id_actividadEconomica = models.ForeignKey(ActividadEconomica, on_delete=models.PROTECT, null= True)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_resolocion = models.DateField(null=False, default="1000-01-01")
    es_aprobado = models.BooleanField("Es aprobado?", null=False, default=False)

    class Meta:
        db_table = 'solicitud'
        ordering = ["id_solicitud"]

    def __str__(self):
        return self.id_solicitud + " - " + self.fecha_solicitud + " - " + self.id_cliente.__str__()



