# Generated by Django 4.1.2 on 2022-10-26 02:58

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_rename_id_pais_region_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domicilio',
            name='region',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='pais', chained_model_field='pais', on_delete=django.db.models.deletion.PROTECT, to='cliente.region', verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='subRegion',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='region', chained_model_field='region', on_delete=django.db.models.deletion.PROTECT, to='cliente.subregion', verbose_name='Sub-Region'),
        ),
    ]
