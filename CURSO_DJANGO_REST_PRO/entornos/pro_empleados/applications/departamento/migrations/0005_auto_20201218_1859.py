# Generated by Django 3.1.4 on 2020-12-19 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0004_auto_20201218_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre corto'),
        ),
    ]
