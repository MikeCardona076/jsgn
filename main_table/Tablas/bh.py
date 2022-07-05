from django.db import models
from main_table.Paciente.paciente_informacion import PacienteInformacion

class BH(models.Model):
    paciente    = models.ForeignKey(PacienteInformacion, on_delete=models.CASCADE)
    plaquetas   = models.CharField(max_length=100, null=True, blank=True)
    monocitos   = models.CharField(max_length=100, null=True, blank=True)
    linfocitos  = models.CharField(max_length=100, null=True, blank=True)
    neutrofilos = models.CharField(max_length=100, null=True, blank=True)
    monocitos   = models.CharField(max_length=100, null=True, blank=True)
    linfocitos  = models.CharField(max_length=100, null=True, blank=True)
    NEUTROFILOS = models.CharField(max_length=100, null=True, blank=True)
    RDW_CV      = models.CharField(max_length=100, null=True, blank=True)
    MCHC    = models.CharField(max_length=100, null=True, blank=True)
    MCH     = models.CharField(max_length=100, null=True, blank=True)
    MCV= models.CharField(max_length=100, null=True, blank=True)
    HEMATOCRITO = models.CharField(max_length=100, null=True, blank=True)
    HEMOGLOBINA = models.CharField(max_length=100, null=True, blank=True)
    GLOBULOS_ROJOS= models.CharField(max_length=100, null=True, blank=True)
    GLOBULOS_BLANCOS =models.CharField(max_length=100, null=True, blank=True)
