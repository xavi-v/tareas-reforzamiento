# Generated by Django 4.2.3 on 2023-07-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('tags', models.CharField(choices=[['critico', 'critico'], ['Medio', 'Medio'], ['bajo', 'bajo'], ['opcional', 'opcional']], default='Opcional', max_length=32)),
            ],
            options={
                'permissions': [('revocar_tarea', 'Recover esta tarea')],
            },
        ),
    ]
