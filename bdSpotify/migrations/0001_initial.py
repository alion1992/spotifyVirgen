# Generated by Django 3.2.25 on 2025-01-16 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('artista', models.CharField(max_length=200)),
                ('album', models.CharField(blank=True, max_length=200, null=True)),
                ('genero', models.CharField(blank=True, max_length=100, null=True)),
                ('duracion', models.IntegerField()),
                ('fecha_lanzamiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('es_activo', models.BooleanField(default=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listas', to='bdSpotify.plan')),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField()),
                ('canciones', models.ManyToManyField(blank=True, null=True, related_name='listas', to='bdSpotify.Cancion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listas', to='bdSpotify.usuario')),
            ],
        ),
    ]