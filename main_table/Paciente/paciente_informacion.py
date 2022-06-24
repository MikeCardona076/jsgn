from django.db import models
import datetime

class PacienteInformacion(models.Model):
    nombre_completo  = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=10, default='M')

    lugar_nacimiento = models.CharField(max_length=100, blank=True, null=True)
    ficha = models.CharField(max_length=100, blank=True, null=True)

    # Return Ficha as primary key
    def __str__(self):
        return self.ficha


