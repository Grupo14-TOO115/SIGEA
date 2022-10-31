# Generated by Django 4.1.2 on 2022-10-30 02:37

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0011_alter_estado_civil_apellidos_conyugue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id_parentesco', models.AutoField(primary_key=True, serialize=False, verbose_name='ID parentesco')),
                ('parentesco', models.CharField(max_length=30, verbose_name='Parentesco')),
            ],
            options={
                'db_table': 'parentesco',
                'ordering': ['id_parentesco'],
            },
        ),
        migrations.CreateModel(
            name='ReferenciaPersonal',
            fields=[
                ('id_referencia', models.AutoField(primary_key=True, serialize=False, verbose_name='ID referencia:')),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('telefono', phone_field.models.PhoneField(blank=True, max_length=13, verbose_name='Telefono')),
                ('parentesco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.parentesco', verbose_name='Parentesco')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.solicitud')),
            ],
            options={
                'db_table': 'referencia personal',
                'ordering': ['id_referencia'],
            },
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id_beneficiario', models.AutoField(primary_key=True, serialize=False)),
                ('porcentaje', models.FloatField(blank=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('telefono', phone_field.models.PhoneField(blank=True, max_length=13, verbose_name='Telefono')),
                ('parentesco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.parentesco')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.solicitud')),
            ],
            options={
                'db_table': 'beneficiario',
                'ordering': ['id_beneficiario'],
            },
        ),
    ]
