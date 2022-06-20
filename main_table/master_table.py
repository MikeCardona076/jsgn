from django.db import models

pruebas = (
    #Numero, Nombre en la db
    ('Quimica Sanguinea 30', 'Quimica Sanguinea 30'),
    ('Biometria Hematica Completa', 'Biometria Hematica Completa'),
    ('Examen General Orina EGO', 'Examen General Orina EGO'),
    ('Antigeno Prostatico Especifico Total', 'Antigeno Prostatico Especifico Total'),
)


class PruebaLaboratorio(models.Model):
    paciente = models.CharField(max_length=100, blank=True)
    clave = models.IntegerField(default=0)
    prueba = models.CharField(max_length=100, blank=True)
    estudio = models.CharField(max_length=100, blank=True)
    resultado = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)

    #If paciente does not exist, then pass it to the next one




class EstudiosLaboratorio(models.Model):
    clave = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=100, blank=True)

 
