# Generated by Django 4.0.5 on 2022-06-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_table', '0002_alter_pruebalaboratorio_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pruebalaboratorio',
            name='clave',
        ),
        migrations.AddField(
            model_name='pruebalaboratorio',
            name='fecha_nacimiento',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
