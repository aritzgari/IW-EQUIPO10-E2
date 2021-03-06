# Generated by Django 3.0.4 on 2020-04-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('DNI', models.CharField(max_length=9)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=25)),
                ('marca', models.CharField(max_length=25)),
                ('categoria', models.CharField(max_length=50)),
                ('fechaadquision', models.DateField()),
                ('fechainstalacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoorden', models.CharField(max_length=10)),
                ('codigoproceso', models.IntegerField()),
                ('nombreproceso', models.CharField(max_length=50)),
                ('referencia', models.CharField(max_length=10)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
            ],
        ),
    ]
