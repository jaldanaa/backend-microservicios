# Generated by Django 4.1.3 on 2022-11-17 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=100)),
                ('nivel_educativo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=150)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grado_cursos', to='grado.grado')),
            ],
        ),
    ]