# Generated by Django 3.1.4 on 2020-12-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('short_name', models.CharField(max_length=50, verbose_name='Nombre corto')),
                ('anulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
    ]
