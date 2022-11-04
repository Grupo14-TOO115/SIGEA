# Generated by Django 4.1.3 on 2022-11-03 08:22

import cliente.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ActividadEconomica",
            fields=[
                (
                    "id_actividadEconomica",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="Actividad Economica ID",
                    ),
                ),
                (
                    "nombreProfesion",
                    models.CharField(
                        max_length=50, verbose_name="Profesion u Ocupacion"
                    ),
                ),
                (
                    "lugarTrabajo",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Nombre de Lugar de trabajo o Negocio",
                    ),
                ),
                (
                    "localidad",
                    models.CharField(
                        help_text="<em>Colonia, Ubanizacion, etc.</em>.",
                        max_length=50,
                        verbose_name="Localidad",
                    ),
                ),
                (
                    "telefono",
                    phone_field.models.PhoneField(
                        blank=True,
                        max_length=13,
                        null=True,
                        verbose_name="Telefono de lugar de trabajo",
                    ),
                ),
                (
                    "asociacion",
                    models.CharField(
                        blank=True,
                        help_text="Ayuda: <em>Puede ser asociacion economica o social</em>.",
                        max_length=50,
                        null=True,
                        verbose_name="Asociaciones a la que pertenece",
                    ),
                ),
            ],
            options={
                "db_table": "ActividadEconomica",
            },
        ),
        migrations.CreateModel(
            name="Anexo",
            fields=[
                ("id_anexo", models.AutoField(primary_key=True, serialize=False)),
                (
                    "dui",
                    models.ImageField(upload_to="fotografias/", verbose_name="DUI"),
                ),
                (
                    "nit",
                    models.ImageField(upload_to="fotografias/", verbose_name="NIT"),
                ),
                (
                    "pasaporte",
                    models.ImageField(
                        upload_to="fotografias/", verbose_name="Pasaporte"
                    ),
                ),
                (
                    "isss",
                    models.ImageField(
                        upload_to="fotografias/", verbose_name="Tarjeta ISSS"
                    ),
                ),
                (
                    "iva",
                    models.ImageField(
                        upload_to="fotografias/", verbose_name="Tarjeta IVA"
                    ),
                ),
            ],
            options={
                "db_table": "anexo",
                "ordering": ["id_anexo"],
            },
        ),
        migrations.CreateModel(
            name="CapacidadEconomica",
            fields=[
                (
                    "id_capacidadEconomica",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="Capacidad Economica ID",
                    ),
                ),
                (
                    "salario",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Salario",
                    ),
                ),
                (
                    "gastosAFP",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Descuento de AFP",
                    ),
                ),
                (
                    "gastosISSS",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Descuento de ISSS",
                    ),
                ),
                (
                    "gastosPersonales",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Gastos Personales",
                    ),
                ),
                (
                    "prestamos",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Prestamos Bancarios",
                    ),
                ),
                (
                    "gastosEducacion",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Gastos de Educacion",
                    ),
                ),
                (
                    "otrosIngresos",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Otros Ingresos",
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=12,
                        verbose_name="Total Capacidad Econoomica",
                    ),
                ),
            ],
            options={
                "db_table": "CapacidadEconomica",
                "ordering": ["id_capacidadEconomica"],
            },
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id_cliente",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Cliente ID"
                    ),
                ),
                ("nombres", models.CharField(max_length=30)),
                ("apellidos", models.CharField(max_length=30)),
                (
                    "identificacion",
                    models.CharField(
                        max_length=20, verbose_name="N° de identificacion"
                    ),
                ),
                (
                    "fecha_nacimiento",
                    models.DateField(
                        help_text="Consejo: <em>Presione en el calendario</em>.",
                        validators=[cliente.models.validar_edad],
                        verbose_name="Fecha de nacimiento",
                    ),
                ),
                ("telefono", phone_field.models.PhoneField(max_length=13)),
                ("correo", models.EmailField(max_length=35, unique=True)),
                (
                    "fotografia",
                    models.ImageField(blank=True, null=True, upload_to="fotografias/"),
                ),
                (
                    "es_asociado",
                    models.BooleanField(default=False, verbose_name="Es asociado?"),
                ),
            ],
            options={
                "db_table": "cliente",
                "ordering": ["id_cliente"],
            },
        ),
        migrations.CreateModel(
            name="EstadoDomicilio",
            fields=[
                (
                    "id_estadoDomicilio",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="Estado domicilio ID",
                    ),
                ),
                ("nombre_estadoDomicilio", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "estadoDomicilio",
                "ordering": ["id_estadoDomicilio"],
            },
        ),
        migrations.CreateModel(
            name="Genero",
            fields=[
                ("id_genero", models.AutoField(primary_key=True, serialize=False)),
                ("genero", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "genero",
            },
        ),
        migrations.CreateModel(
            name="Pais",
            fields=[
                (
                    "id_pais",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Pais ID"
                    ),
                ),
                ("codigo_pais", models.CharField(max_length=50)),
                ("nombre_pais", models.CharField(max_length=50)),
                ("area_pais", models.IntegerField()),
            ],
            options={
                "db_table": "pais",
                "ordering": ["id_pais"],
            },
        ),
        migrations.CreateModel(
            name="Parentesco",
            fields=[
                (
                    "id_parentesco",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="ID parentesco"
                    ),
                ),
                (
                    "parentesco",
                    models.CharField(max_length=30, verbose_name="Parentesco"),
                ),
            ],
            options={
                "db_table": "parentesco",
                "ordering": ["id_parentesco"],
            },
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id_region",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Region ID"
                    ),
                ),
                ("nombre_region", models.CharField(max_length=50)),
                (
                    "pais",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.pais",
                        verbose_name="Pais",
                    ),
                ),
            ],
            options={
                "db_table": "region",
                "ordering": ["id_region"],
            },
        ),
        migrations.CreateModel(
            name="situacionLaboral",
            fields=[
                (
                    "id_situacionLaboral",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="Situacion Laboral ID",
                    ),
                ),
                (
                    "nombre_situacionLaboral",
                    models.CharField(
                        max_length=50, verbose_name="Situacion laboral actual"
                    ),
                ),
            ],
            options={
                "db_table": "situacionLaboral",
                "ordering": ["id_situacionLaboral"],
            },
        ),
        migrations.CreateModel(
            name="tipo_Estadocivil",
            fields=[
                (
                    "id_tipoEstadocivil",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("nombre_tipoEstadocivil", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "tipo_estadocivil",
            },
        ),
        migrations.CreateModel(
            name="TipoIdentificacion",
            fields=[
                (
                    "id_tipoIdentificacion",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("nombreTipoIdentificacion", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "tipo_identificacion",
            },
        ),
        migrations.CreateModel(
            name="Ubicacioneografica",
            fields=[
                (
                    "id_ubicacion",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Ubicacion ID"
                    ),
                ),
                ("direccion", models.CharField(max_length=50)),
                ("latitud", models.FloatField()),
                ("longitud", models.FloatField()),
            ],
            options={
                "db_table": "ubicacion_google",
                "ordering": ["id_ubicacion"],
            },
        ),
        migrations.CreateModel(
            name="UbicacionGeografica",
            fields=[
                (
                    "id_ubicacion",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Ubicacion ID"
                    ),
                ),
                ("direccion", models.CharField(max_length=50)),
                ("latitud", models.FloatField()),
                ("longitud", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="SubRegion",
            fields=[
                (
                    "id_subRegion",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Sub-Region ID"
                    ),
                ),
                ("nombre_subRegion", models.CharField(max_length=50)),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.region",
                        verbose_name="Region",
                    ),
                ),
            ],
            options={
                "db_table": "subRegion",
                "ordering": ["id_subRegion"],
            },
        ),
        migrations.CreateModel(
            name="Solicitud",
            fields=[
                (
                    "id_solicitud",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Solicitud ID"
                    ),
                ),
                ("fecha_solicitud", models.DateField(auto_now_add=True)),
                ("fecha_resolocion", models.DateField(default="1000-01-01")),
                (
                    "es_aprobado",
                    models.BooleanField(default=False, verbose_name="Es aprobado?"),
                ),
                (
                    "es_revisado",
                    models.BooleanField(default=False, verbose_name="Es revisado?"),
                ),
                (
                    "es_validado",
                    models.BooleanField(default=False, verbose_name="Es validado?"),
                ),
                (
                    "id_actividadEconomica",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.actividadeconomica",
                    ),
                ),
                (
                    "id_anexo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.anexo",
                    ),
                ),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.cliente",
                    ),
                ),
            ],
            options={
                "db_table": "solicitud",
                "ordering": ["id_solicitud"],
            },
        ),
        migrations.CreateModel(
            name="ReferenciaPersonal",
            fields=[
                (
                    "id_referencia",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="ID referencia:"
                    ),
                ),
                ("nombres", models.CharField(max_length=30, verbose_name="Nombres")),
                (
                    "apellidos",
                    models.CharField(max_length=30, verbose_name="Apellidos"),
                ),
                (
                    "telefono",
                    phone_field.models.PhoneField(
                        blank=True, max_length=13, verbose_name="Telefono"
                    ),
                ),
                (
                    "parentesco",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cliente.parentesco",
                        verbose_name="Parentesco",
                    ),
                ),
                (
                    "solicitud",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cliente.solicitud",
                    ),
                ),
            ],
            options={
                "db_table": "referencia personal",
                "ordering": ["id_referencia"],
            },
        ),
        migrations.CreateModel(
            name="estado_civil",
            fields=[
                (
                    "id_estadocivil",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID Estado Civil",
                    ),
                ),
                (
                    "nombres_conyugue",
                    models.CharField(
                        blank=True,
                        help_text="Ayuda: <em>Solo ingresar estos datos si está casado o comprometido.</em>.",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "apellidos_conyugue",
                    models.CharField(
                        blank=True,
                        help_text="Ayuda: <em>Solo ingresar estos datos si está casado o comprometido.</em>.",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "telefono",
                    phone_field.models.PhoneField(
                        blank=True,
                        help_text="Ayuda: <em>Solo ingresar estos datos si está casado o comprometido.</em>.",
                        max_length=13,
                        null=True,
                    ),
                ),
                (
                    "id_tipoEstadocivil",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.tipo_estadocivil",
                        verbose_name="Estado civil",
                    ),
                ),
            ],
            options={
                "db_table": "estado_civil",
                "ordering": ["id_estadocivil"],
            },
        ),
        migrations.CreateModel(
            name="Domicilio",
            fields=[
                (
                    "id_domicilio",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Domicilio ID"
                    ),
                ),
                (
                    "tiempo_de_inmueble",
                    models.PositiveIntegerField(
                        help_text="Ayuda: <em>Tiempo en meses</em>.",
                        verbose_name="Tiempo en el inmueble",
                    ),
                ),
                (
                    "localidad",
                    models.CharField(
                        help_text="<em>Colonia, Ubanizacion, etc.</em>.",
                        max_length=50,
                        verbose_name="Localidad",
                    ),
                ),
                (
                    "cliente",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cliente.cliente",
                    ),
                ),
                (
                    "estadoDomicilio",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.estadodomicilio",
                        verbose_name="Estado del domicilio",
                    ),
                ),
                (
                    "pais",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.pais",
                        verbose_name="Pais",
                    ),
                ),
                (
                    "region",
                    smart_selects.db_fields.ChainedForeignKey(
                        auto_choose=True,
                        chained_field="pais",
                        chained_model_field="pais",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.region",
                        verbose_name="Region / Estado",
                    ),
                ),
                (
                    "subRegion",
                    smart_selects.db_fields.ChainedForeignKey(
                        auto_choose=True,
                        chained_field="region",
                        chained_model_field="region",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.subregion",
                        verbose_name="Sub-Region / Ciudad",
                    ),
                ),
            ],
            options={
                "db_table": "domicilio",
                "ordering": ["id_domicilio"],
            },
        ),
        migrations.AddField(
            model_name="cliente",
            name="id_estadocivil",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.estado_civil",
            ),
        ),
        migrations.AddField(
            model_name="cliente",
            name="id_genero",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.genero",
                verbose_name="Genero",
            ),
        ),
        migrations.AddField(
            model_name="cliente",
            name="id_tipoIdentificacion",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.tipoidentificacion",
                verbose_name="Tipo de identificacion",
            ),
        ),
        migrations.CreateModel(
            name="Beneficiario",
            fields=[
                (
                    "id_beneficiario",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("porcentaje", models.IntegerField(blank=True)),
                ("nombres", models.CharField(max_length=30)),
                ("apellidos", models.CharField(max_length=30)),
                (
                    "telefono",
                    phone_field.models.PhoneField(
                        blank=True, max_length=13, verbose_name="Telefono"
                    ),
                ),
                (
                    "parentesco",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cliente.parentesco",
                    ),
                ),
                (
                    "solicitud",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cliente.solicitud",
                    ),
                ),
            ],
            options={
                "db_table": "beneficiario",
                "ordering": ["id_beneficiario"],
            },
        ),
        migrations.AddField(
            model_name="actividadeconomica",
            name="id_capacidadEconomica",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.capacidadeconomica",
                verbose_name="Capacidad Economica",
            ),
        ),
        migrations.AddField(
            model_name="actividadeconomica",
            name="pais",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.pais",
                verbose_name="Pais",
            ),
        ),
        migrations.AddField(
            model_name="actividadeconomica",
            name="region",
            field=smart_selects.db_fields.ChainedForeignKey(
                auto_choose=True,
                chained_field="pais",
                chained_model_field="pais",
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.region",
                verbose_name="Region / Estado",
            ),
        ),
        migrations.AddField(
            model_name="actividadeconomica",
            name="situacionLaboral",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.situacionlaboral",
                verbose_name="Situacion laboral actual",
            ),
        ),
        migrations.AddField(
            model_name="actividadeconomica",
            name="subRegion",
            field=smart_selects.db_fields.ChainedForeignKey(
                auto_choose=True,
                chained_field="region",
                chained_model_field="region",
                on_delete=django.db.models.deletion.PROTECT,
                to="cliente.subregion",
                verbose_name="Sub-Region / Ciudad",
            ),
        ),
    ]
