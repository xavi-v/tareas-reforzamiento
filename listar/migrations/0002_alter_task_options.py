# Generated by Django 4.2.3 on 2023-07-15 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': [('revocar_tarea', 'Revocar esta tarea')], 'verbose_name_plural': 'Administrar Tarea'},
        ),
    ]
