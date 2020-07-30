# Generated by Django 3.0.8 on 2020-07-17 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media/imagenes/')),
                ('fecha_hora_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_publicaciones', to=settings.AUTH_USER_MODEL)),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasificacion_publicaciones', to='publicaciones.Clasificacion')),
            ],
        ),
    ]
