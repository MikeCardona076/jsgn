# Generated by Django 4.0.5 on 2022-06-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_table', '0003_remove_pruebalaboratorio_clave_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pruebalaboratorio',
            name='nombre_paciente',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
