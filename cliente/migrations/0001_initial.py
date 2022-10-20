# Generated by Django 4.1.2 on 2022-10-18 03:02

import cliente.models
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEconomica',
            fields=[
                ('id_actividadEconomica', models.AutoField(primary_key=True, serialize=False, verbose_name='Actividad Economica ID')),
                ('lugarTrabajo', models.CharField(max_length=50)),
                ('telefono', phone_field.models.PhoneField(max_length=13)),
            ],
            options={
                'db_table': 'ActividadEconomica',
            },
        ),
        migrations.CreateModel(
            name='CapacidadEconomica',
            fields=[
                ('id_capacidadEconomica', models.AutoField(primary_key=True, serialize=False, verbose_name='Capacidad Economica ID')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('gastosAFP', models.DecimalField(decimal_places=2, max_digits=8)),
                ('gastosPersonales', models.DecimalField(decimal_places=2, max_digits=8)),
                ('prestamos', models.DecimalField(decimal_places=2, max_digits=8)),
                ('gastosEducacion', models.DecimalField(decimal_places=2, max_digits=8)),
                ('otrosIngresos', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Capacidad Economica')),
            ],
            options={
                'db_table': 'CapacidadEconomica',
                'ordering': ['id_capacidadEconomica'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Cliente ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('identificacion', models.CharField(max_length=20, verbose_name='N° de identificacion')),
                ('fecha_nacimiento', models.DateField(help_text='Consejo: <em>Presione en el calendario</em>.', validators=[cliente.models.validar_edad], verbose_name='Fecha de nacimiento')),
                ('telefono', phone_field.models.PhoneField(max_length=13)),
                ('correo', models.EmailField(max_length=35)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to='fotografias/')),
                ('es_asociado', models.BooleanField(default=False, verbose_name='Es asociado?')),
            ],
            options={
                'db_table': 'cliente',
                'ordering': ['id_cliente'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'genero',
            },
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id_profesion', models.AutoField(primary_key=True, serialize=False, verbose_name='Profesion ID')),
                ('nombre_profesion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'profesion',
                'ordering': ['id_profesion'],
            },
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id_tipoIdentificacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreTipoIdentificacion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_identificacion',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False, verbose_name='Solicitud ID')),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('fecha_resolocion', models.DateField(default='1000-01-01')),
                ('es_aprobado', models.BooleanField(default=False, verbose_name='Es aprobado?')),
                ('id_actividadEconomica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.actividadeconomica')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.cliente')),
            ],
            options={
                'db_table': 'solicitud',
                'ordering': ['id_solicitud'],
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_genero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cliente.genero', verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_tipoIdentificacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cliente.tipoidentificacion', verbose_name='Tipo de identificacion'),
        ),
        migrations.AddField(
            model_name='actividadeconomica',
            name='id_capacidadEconomica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.capacidadeconomica'),
        ),
        migrations.AddField(
            model_name='actividadeconomica',
            name='id_profesion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.profesion'),
        ),
    ]
