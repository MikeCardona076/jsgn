from django.forms import model_to_dict
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
import pandas as pd

########### Modelos ###############
from .Paciente.paciente_informacion import PacienteInformacion
from .master_table import EstudiosLaboratorio, PruebaLaboratorio

from .Tablas.qs30 import QS30

def get_guerreo_negro(request):
    pacientes_guerrero_negro =  PacienteInformacion.objects.filter(lugar_nacimiento = 'Guerrero Negro').values()

    df = pd.DataFrame(pacientes_guerrero_negro)

    df.to_excel("Pacientes_Guerrero.xlsx")

    with open('Pacientes_Guerrero.xlsx', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Pacientes_Guerrero.xlsx"'
        return response


##############################################################################################################
def get_Islacedros(request):

    try:
        pacientes_isladecedros =  PacienteInformacion.objects.filter(lugar_nacimiento = 'Isla de Cedros',  edad__isnull = False).values()

        df = pd.DataFrame(pacientes_isladecedros)

        df.to_excel("Isladecedros.xlsx")

        with open('Isladecedros.xlsx', 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Isladecedros.xlsx"'
            return response

    except Exception as e:
        return HttpResponse(e)



##############################################################################################################
