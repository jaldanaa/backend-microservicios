# Generated by Django 4.1.3 on 2022-11-22 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='padres_representantes',
            name='parentesco_alumno',
            field=models.TextField(default=0, verbose_name=50),
            preserve_default=False,
        ),
    ]