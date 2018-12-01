# Generated by Django 2.0.7 on 2018-10-27 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Raza'),
        ),
    ]
