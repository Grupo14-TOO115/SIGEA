from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from phone_field import PhoneField
from django.contrib.auth.models import User
from datetime import date
from django.utils.translation import gettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey

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
    nombres_conyugue = models.CharField(max_length=30, null=True, blank=True, help_text="Ayuda: <em>Solo ingresar estos datos si está casado o comprometido.</em>.")
    apellidos_conyugue = models.CharField(max_length=30, null=True, blank=True, help_text="Ayuda: <em>Solo ingresar estos datos si está casado o comprometido.</em>.")
    telefono = PhoneField(max_length=13, null=True, blank=True, help_text="Ayuda: <em>Solo ingresar estos datos si está casado o comprometido.</em>.")

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
    correo = models.EmailField(max_length=35,  null=False, blank=False, unique=True)
    fotografia = models.ImageField(upload_to='fotografias/', null=True, blank=True)
    es_asociado = models.BooleanField("Es asociado?", null=False, default=False)


    class Meta:
        db_table = 'cliente'
        ordering = ["id_cliente"]

    def __str__(self):
        return self.id_cliente.__str__() + " - " + self.nombres + " - " + self.apellidos + " - " + self.identificacion


class situacionLaboral(models.Model):
    id_situacionLaboral = models.AutoField(primary_key=True, verbose_name="Situacion Laboral ID")
    nombre_situacionLaboral= models.CharField("Situacion laboral actual", max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'situacionLaboral'
        ordering = ["id_situacionLaboral"]

    def __str__(self):
        return self.nombre_situacionLaboral


class CapacidadEconomica(models.Model):
    id_capacidadEconomica = models.AutoField(primary_key=True, verbose_name="Capacidad Economica ID")
    salario = models.DecimalField("Salario", max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosAFP = models.DecimalField("Descuento de AFP", max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosISSS = models.DecimalField("Descuento de ISSS", max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosPersonales = models.DecimalField("Gastos Personales", max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    prestamos = models.DecimalField("Prestamos Bancarios", max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    gastosEducacion = models.DecimalField("Gastos de Educacion", max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    otrosIngresos = models.DecimalField("Otros Ingresos",max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0)])
    total = models.DecimalField("Total Capacidad Econoomica", max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'CapacidadEconomica'
        ordering = ["id_capacidadEconomica"]

    def __str__(self):
        return self.id_capacidad + " - " + self.total


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


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True, verbose_name="Pais ID")
    codigo_pais = models.CharField(max_length=50, null=False, blank=False)
    nombre_pais = models.CharField(max_length=50, null=False, blank=False)
    area_pais = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'pais'
        ordering = ["id_pais"]

    def __str__(self):
        return self.codigo_pais + " - " + self.nombre_pais


class Region(models.Model):
    id_region = models.AutoField(primary_key=True, verbose_name="Region ID")
    nombre_region = models.CharField(max_length=50, null=False, blank=False)
    pais = models.ForeignKey(Pais, verbose_name="Pais", on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        db_table = 'region'
        ordering = ["id_region"]

    def __str__(self):
        return self.nombre_region


class SubRegion(models.Model):
    id_subRegion = models.AutoField(primary_key=True, verbose_name="Sub-Region ID")
    nombre_subRegion = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, verbose_name="Region", on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        db_table = 'subRegion'
        ordering = ["id_subRegion"]

    def __str__(self):
        return self.nombre_subRegion


class ActividadEconomica(models.Model):
    id_actividadEconomica = models.AutoField(primary_key=True, verbose_name="Actividad Economica ID")
    id_capacidadEconomica = models.ForeignKey(CapacidadEconomica, verbose_name="Capacidad Economica",on_delete=models.PROTECT,null= True)
    situacionLaboral = models.ForeignKey(situacionLaboral, verbose_name="Situacion laboral actual",on_delete=models.PROTECT, null=False, default=1)
    nombreProfesion = models.CharField("Profesion u Ocupacion", max_length=50, null=False, blank=False)
    lugarTrabajo = models.CharField("Nombre de Lugar de trabajo o Negocio",max_length=50, null=True, blank=True)
    pais = models.ForeignKey(Pais, verbose_name="Pais", on_delete=models.PROTECT, null=False, blank=False, default=1)
    region = ChainedForeignKey(Region, chained_field="pais", chained_model_field='pais', auto_choose=True, show_all=False, verbose_name="Region / Estado", on_delete=models.PROTECT, null=False, blank=False)
    subRegion = ChainedForeignKey(SubRegion, chained_field="region", chained_model_field='region', auto_choose=True, show_all=False, verbose_name="Sub-Region / Ciudad", on_delete=models.PROTECT, null=False, blank=False)
    localidad = models.CharField("Localidad", max_length=50, null=False, blank=False, help_text="<em>Colonia, Ubanizacion, etc.</em>.")
    telefono = PhoneField("Telefono de lugar de trabajo",max_length=13, null=True, blank=True)
    asociacion = models.CharField("Asociaciones a la que pertenece",max_length=50, null=True, blank=True, help_text="Ayuda: <em>Puede ser asociacion economica o social</em>.")

    class Meta:
        db_table = 'ActividadEconomica'

    def __str__(self):
        return self.id_actividadEconomica + " - " + self.id_capacidadEconomica + " - " + self.id_profesion


class UbicacionGeografica(models.Model):
    id_ubicacion = models.AutoField(primary_key=True, verbose_name="Ubicacion ID")
    direccion = models.CharField(max_length=50, null=False, blank=False)
    latitud = models.FloatField(null=False, blank=False)
    longitud = models.FloatField(null=False, blank=False)


class EstadoDomicilio(models.Model):
    id_estadoDomicilio = models.AutoField(primary_key=True, verbose_name="Estado domicilio ID")
    nombre_estadoDomicilio = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'estadoDomicilio'
        ordering = ["id_estadoDomicilio"]

    def __str__(self):
        return self.nombre_estadoDomicilio


class Domicilio(models.Model):
    id_domicilio=models.AutoField(primary_key=True, verbose_name="Domicilio ID")
    tiempo_de_inmueble=models.PositiveIntegerField(null=False, blank=False, verbose_name="Tiempo en el inmueble", help_text="Ayuda: <em>Tiempo en meses</em>.")
    estadoDomicilio = models.ForeignKey(EstadoDomicilio, verbose_name="Estado del domicilio", on_delete=models.PROTECT, null=False, blank=False, default=1)
    pais = models.ForeignKey(Pais, verbose_name="Pais", on_delete=models.PROTECT, null=False, blank=False, default=1)
    region = ChainedForeignKey(Region, chained_field="pais", chained_model_field='pais', auto_choose=True,
                                 show_all=False, verbose_name="Region / Estado", on_delete=models.PROTECT, null=False,
                                 blank=False)
    subRegion = ChainedForeignKey(SubRegion, chained_field="region", chained_model_field='region', auto_choose=True,
                                  show_all=False, verbose_name="Sub-Region / Ciudad", on_delete=models.PROTECT, null=False,
                                  blank=False)
    localidad = models.CharField("Localidad", max_length=50, null=False, blank=False,
                                 help_text="<em>Colonia, Ubanizacion, etc.</em>.")
    cliente=models.OneToOneField(Cliente, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table='domicilio'
        ordering=["id_domicilio"]

    def __str__(self):
        return str(self.tiempo_de_inmueble)


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True, verbose_name="Solicitud ID")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)
    id_actividadEconomica = models.ForeignKey(ActividadEconomica, on_delete=models.PROTECT, null= True)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_resolocion = models.DateField(null=False, default="1000-01-01")
    es_aprobado = models.BooleanField("Es aprobado?", null=False, default=False)
    es_revisado = models.BooleanField("Es revisado?", null=False, default=False)
    es_validado = models.BooleanField("Es validado?", null=False, default=False)

    class Meta:
        db_table = 'solicitud'
        ordering = ["id_solicitud"]

    def __str__(self):
        return self.id_solicitud + " - " + self.fecha_solicitud + " - " + self.id_cliente.__str__()



class Parentesco(models.Model):
    id_parentesco=models.AutoField(primary_key=True, verbose_name='ID parentesco')
    parentesco=models.CharField(max_length=30, null=False, blank=False, verbose_name='Parentesco')

    class Meta:
        db_table='parentesco'
        ordering=["id_parentesco"]

    def __str__(self):
        return self.parentesco

class ReferenciaPersonal(models.Model):
    id_referencia=models.AutoField(primary_key=True, verbose_name='ID referencia:')
    solicitud=models.ForeignKey(Solicitud,on_delete=models. CASCADE, null=False, blank=False)
    parentesco=models.ForeignKey(Parentesco,on_delete=models.CASCADE,null=False, blank=False, verbose_name='Parentesco', default=1)
    nombres=models.CharField(max_length=30, null=False, blank=False,verbose_name='Nombres')
    apellidos=models.CharField(max_length=30, null=False, blank=False,verbose_name='Apellidos')
    telefono=PhoneField(max_length=13, null=False, blank=True,verbose_name='Telefono')

    class Meta:
        db_table='referencia personal'
        ordering=['id_referencia']

    def __str__(self):
        return self.parentesco.__str__()+' - '+self.nombres+' - '+self.apellidos

class Beneficiario(models.Model):
    id_beneficiario=models.AutoField(primary_key=True)
    solicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE, null=False, blank=False)
    parentesco=models.ForeignKey(Parentesco, on_delete=models.CASCADE, null=False, blank=False)
    porcentaje=models.FloatField(null=False,blank=True)
    nombres=models.CharField(max_length=30, null=False, blank=False)
    apellidos=models.CharField(max_length=30,null=False,blank=False)
    telefono=PhoneField(max_length=13, null=False, blank=True,verbose_name='Telefono')

    class Meta:
        db_table='beneficiario'
        ordering=['id_beneficiario']

    def __str__(self):
        return self.id_beneficiario.__str__()+' - '+self.parentesco.__str__()+' - '+str(self.porcentaje)+' - '+self.nombres+' - '+self.apellidos

class Anexo(models.Model):
    id_anexo=models.AutoField(primary_key=True)
    solicitud=models.ForeignKey(Solicitud, on_delete=models.CASCADE, null=False, blank=False)
    dui=models.ImageField(upload_to='fotografias/',verbose_name="DUI",null=False,blank=False)
    nit=models.ImageField(upload_to='fotografias/',verbose_name="NIT",null=False,blank=False)
    pasaporte=models.ImageField(upload_to='fotografias/',verbose_name="Pasaporte",null=False,blank=False)
    isss=models.ImageField(upload_to='fotografias/',verbose_name="Tarjeta ISSS",null=False,blank=False)
    iva=models.ImageField(upload_to='fotografias/',verbose_name="Tarjeta IVA",null=False,blank=False)

    class Meta:
        db_table='anexo'
        ordering=['id_anexo']

    def __str__(self):
        return self.id_anexo.__str__()+' - '+self.solicitud.id_solicitud.__str__()

