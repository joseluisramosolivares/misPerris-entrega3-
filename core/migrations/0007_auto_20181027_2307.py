# Generated by Django 2.1.2 on 2018-10-28 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181027_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='raza',
            options={'verbose_name': 'Raza', 'verbose_name_plural': 'Razas'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regiones'},
        ),
    ]
