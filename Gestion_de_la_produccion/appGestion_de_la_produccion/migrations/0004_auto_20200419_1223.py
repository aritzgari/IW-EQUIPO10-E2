# Generated by Django 3.0.4 on 2020-04-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGestion_de_la_produccion', '0003_auto_20200419_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='fechaadquision',
            new_name='fecha_adquision',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='fechainstalacion',
            new_name='fecha_instalacion',
        ),
        migrations.RenameField(
            model_name='proceso',
            old_name='codigoorden',
            new_name='codigo_orden',
        ),
        migrations.RenameField(
            model_name='proceso',
            old_name='nombreproceso',
            new_name='nombre_proceso',
        ),
        migrations.RemoveField(
            model_name='proceso',
            name='codigoproceso',
        ),
        migrations.AddField(
            model_name='proceso',
            name='codigo_proceso',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
