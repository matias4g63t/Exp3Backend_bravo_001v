# Generated by Django 3.2.4 on 2021-06-22 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Aeronave',
            fields=[
                ('numeroSerie', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Numero serie')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca Aeronave')),
                ('modelo', models.CharField(max_length=20, verbose_name='Modelo de la aeronave')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_dron.categoria')),
            ],
        ),
    ]