# Generated by Django 3.2.4 on 2021-06-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_colaborador_rutcolaborador'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='correo',
            field=models.CharField(default=0, max_length=50, verbose_name='Correo'),
            preserve_default=False,
        ),
    ]
