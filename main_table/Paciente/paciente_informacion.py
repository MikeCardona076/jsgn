from django.db import models
import datetime

class PacienteInformacion(models.Model):
    LISTA_CLASIFICACION = (
        ('Bajo Peso', 'Bajo Peso'),
        ('Peso Ideal', 'Peso Ideal'),
        ('Sobrepeso', 'Sobrepeso'),
        ('Obesidad', 'Obesidad'),
        ('Obesidad Severa', 'Obesidad Severa'),
        ('Obesidad Mórbida', 'Obesidad Mórbida'),
    )



    nombre_completo  = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=10, default='M')
    lugar_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    ficha = models.CharField(max_length=100, blank=True, null=True)
    curp = models.CharField(max_length=100, blank=True, null=True)
    edad  = models.CharField(max_length=100, blank=True, null=True)
    medicion_cintura = models.CharField(max_length=100, blank=True, null=True)
    indice_de_masa_corporal = models.CharField(max_length=100, blank=True, null=True)
    aumento_trigliceridos  = models.CharField(max_length=100, blank=True, null=True)
    aumento_colesterol_HDL = models.CharField(max_length=100, blank=True, null=True)
    tension_arterial = models.CharField(max_length=100, blank=True, null=True)
    medicacion_anti_hipertensiva  = models.CharField(max_length=100, blank=True, null=True)
    glicemia_ayunas  = models.CharField(max_length=100, blank=True, null=True)
    talla = models.CharField(max_length=100, blank=True, null=True)
    peso = models.CharField(max_length=100, blank=True, null=True)
    clasificacion_de_obesidad = models.CharField(max_length=100, choices=LISTA_CLASIFICACION, blank=True, null=True)
    antecedentes_diabetes = models.CharField(max_length=100, blank=True, null=True, default='No')
    consentimiento_informado = models.CharField(max_length=100, blank=True, null=True, default='No')
    

    # Return Ficha as primary key
    def __str__(self):
        return self.ficha


