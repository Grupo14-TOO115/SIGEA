# Generated by Django 4.1.2 on 2022-10-26 03:40

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_rename_pais_domicilio_id_pais_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domicilio',
            old_name='id_pais',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='id_pais',
            new_name='pais',
        ),
        migrations.RenameField(
            model_name='subregion',
            old_name='id_region',
            new_name='region',
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='region',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='pais', chained_model_field='pais', on_delete=django.db.models.deletion.PROTECT, to='cliente.region', verbose_name='Region'),
        ),
    ]
