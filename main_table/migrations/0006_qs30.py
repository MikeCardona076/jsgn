# Generated by Django 4.0.5 on 2022-06-30 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_table', '0005_pacienteinformacion_aumento_colesterol_hdl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QS30',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatinina', models.CharField(blank=True, max_length=100, null=True)),
                ('colesterol_Total', models.CharField(blank=True, max_length=100, null=True)),
                ('trigliceridos', models.CharField(blank=True, max_length=100, null=True)),
                ('acido_Urico_Serico', models.CharField(blank=True, max_length=100, null=True)),
                ('proteinas_Totales', models.CharField(blank=True, max_length=100, null=True)),
                ('albumina_Serica', models.CharField(blank=True, max_length=100, null=True)),
                ('globulina', models.CharField(blank=True, max_length=100, null=True)),
                ('deshidrogenasa_Lactica', models.CharField(blank=True, max_length=100, null=True)),
                ('transaminasa_Glutamico_Oxalacetica', models.CharField(blank=True, max_length=100, null=True)),
                ('transaminasa_Glutamico_Piruvica', models.CharField(blank=True, max_length=100, null=True)),
                ('fosfatasa_Alcalina', models.CharField(blank=True, max_length=100, null=True)),
                ('gammaglutamil_Transpeptidasa', models.CharField(blank=True, max_length=100, null=True)),
                ('sodio_Sérico', models.CharField(blank=True, max_length=100, null=True)),
                ('potasio_Sérico', models.CharField(blank=True, max_length=100, null=True)),
                ('cloro_Serico', models.CharField(blank=True, max_length=100, null=True)),
                ('calcio_Serico', models.CharField(blank=True, max_length=100, null=True)),
                ('fosforo_Sérico', models.CharField(blank=True, max_length=100, null=True)),
                ('bilirrubina_Total', models.CharField(blank=True, max_length=100, null=True)),
                ('bilirrubina_Conjugada', models.CharField(blank=True, max_length=100, null=True)),
                ('colesterol_alta_densidad', models.CharField(blank=True, max_length=100, null=True)),
                ('colesterol_Baja_Densidad', models.CharField(blank=True, max_length=100, null=True)),
                ('Indice_Aterogenico', models.CharField(blank=True, max_length=100, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_table.pacienteinformacion')),
            ],
        ),
    ]