# Generated by Django 2.1.2 on 2018-11-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181027_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
    ]
