# Generated by Django 3.1.4 on 2020-12-19 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_auto_20201218_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(blank=True, editable=False, max_length=50, verbose_name='Nombre corto'),
        ),
    ]
