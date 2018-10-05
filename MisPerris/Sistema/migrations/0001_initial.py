# Generated by Django 2.1 on 2018-10-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigoCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=20)),
                ('apellidoCliente', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('codigoMascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombreMascota', models.CharField(max_length=20)),
            ],
        ),
    ]