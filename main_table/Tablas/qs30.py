from django.db import models
from main_table.Paciente.paciente_informacion import PacienteInformacion

class QS30(models.Model):
    paciente = models.ForeignKey(PacienteInformacion, on_delete=models.CASCADE)
    glucosa = models.CharField(max_length=100, null=True, blank=True)#Se toma a Glicemia 
    nitrOgeno_Ureico = models.CharField(max_length=100, null=True, blank=True)
    urea_serica = models.CharField(max_length=100, null=True, blank=True)
    creatinina = models.CharField(max_length=100, null=True, blank=True)
    colesterol_Total= models.CharField(max_length=100, null=True, blank=True)
    trigliceridos = models.CharField(max_length=100, null=True, blank=True) #Se toma
    acido_Urico_Serico = models.CharField(max_length=100, null=True, blank=True)
    proteinas_Totales = models.CharField(max_length=100, null=True, blank=True)
    albumina_Serica = models.CharField(max_length=100, null=True, blank=True)
    globulina = models.CharField(max_length=100, null=True, blank=True)
    deshidrogenasa_Lactica = models.CharField(max_length=100, null=True, blank=True)
    transaminasa_Glutamico_Oxalacetica = models.CharField(max_length=100, null=True, blank=True)
    transaminasa_Glutamico_Piruvica = models.CharField(max_length=100, null=True, blank=True)
    fosfatasa_Alcalina = models.CharField(max_length=100, null=True, blank=True)
    gammaglutamil_Transpeptidasa = models.CharField(max_length=100, null=True, blank=True)
    sodio_Sérico = models.CharField(max_length=100, null=True, blank=True)
    potasio_Sérico = models.CharField(max_length=100, null=True, blank=True)
    cloro_Serico = models.CharField(max_length=100, null=True, blank=True)
    calcio_Serico = models.CharField(max_length=100, null=True, blank=True)
    fosforo_Sérico = models.CharField(max_length=100, null=True, blank=True)
    bilirrubina_Total = models.CharField(max_length=100, null=True, blank=True)
    bilirrubina_Conjugada = models.CharField(max_length=100, null=True, blank=True)
    colesterol_alta_densidad = models.CharField(max_length=100, null=True, blank=True) #Aumento de Colesterol HDL:
    colesterol_Baja_Densidad = models.CharField(max_length=100, null=True, blank=True)
    Indice_Aterogenico = models.CharField(max_length=100, null=True, blank=True)
