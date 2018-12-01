# Generated by Django 2.1.2 on 2018-10-28 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181027_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Estado'),
        ),
    ]
