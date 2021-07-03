# Generated by Django 3.2.4 on 2021-06-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('rutColaborador', models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut de Colaborador')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Imagen')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('telefono', models.CharField(max_length=12, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('pais', models.CharField(max_length=50, verbose_name='pais')),
                ('contraseña', models.CharField(max_length=30, verbose_name='contraseña')),
            ],
        ),
    ]