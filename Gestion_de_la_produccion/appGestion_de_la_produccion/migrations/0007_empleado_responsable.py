# Generated by Django 3.0.4 on 2020-04-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGestion_de_la_produccion', '0006_proceso_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='responsable',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
