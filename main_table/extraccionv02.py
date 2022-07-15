from django.http import  HttpResponse
import pandas as pd

########### Modelos ###############
from .Paciente.paciente_informacion import PacienteInformacion
from .Tablas.qs30 import QS30


import datetime


def pacientes_guerrero_negro_qs30(request):

    pacientes_guerrero_negro = PacienteInformacion.objects.filter(id__in = [ x.paciente.id for x in QS30.objects.all()], lugar_nacimiento = "Guerrero Negro")


    pruebas = QS30.objects.filter(paciente__in = [ x.id for x in pacientes_guerrero_negro]).values()

    columnas_qs30 = [
    'paciente',
    'sexo',
    'Edad',
    'curp',
    'Lugar de Nacimiento',
    'medicion_cintura',
    'indice_de_masa_corporal',
    'aumento_trigliceridos',
    'aumento_colesterol_HDL',
    'tension_arterial' ,
    'medicacion_anti_hipertensiva',
    'glicemia_ayunas',
    #########################################
    'glucosa' ,
    'nitrOgeno_Ureico' ,
    'urea_serica' ,
    'creatinina' ,
    'colesterol_Total',
    'trigliceridos' ,
    'acido_Urico_Serico' ,
    'proteinas_Totales' ,
    'albumina_Serica' ,
    'globulina' ,
    'deshidrogenasa_Lactica' ,
    'transaminasa_Glutamico_Oxalacetica' ,
    'transaminasa_Glutamico_Piruvica' ,
    'fosfatasa_Alcalina' ,
    'gammaglutamil_Transpeptidasa' ,
    'sodio_Sérico' ,
    'potasio_Sérico' ,
    'cloro_Serico' ,
    'calcio_Serico' ,
    'fosforo_Sérico' ,
    'bilirrubina_Total' ,
    'bilirrubina_Conjugada' ,
    'colesterol_alta_densidad' ,
    'colesterol_Baja_Densidad' ,
    'Indice_Aterogenico' 
    'antecedentes_diabetes',
    'consentimiento_informado',
    ]

    df = pd.DataFrame(pruebas, index=None, columns=columnas_qs30)

    df['paciente'] = [ x.nombre_completo for x in pacientes_guerrero_negro]
    df['sexo'] = [ x.sexo for x in pacientes_guerrero_negro]
    df['Lugar de Nacimiento'] = [ x.lugar_nacimiento for x in pacientes_guerrero_negro]
    df['Edad'] = [ x.fecha_nacimiento for x in pacientes_guerrero_negro]
    df['medicion_cintura'] = [ x.medicion_cintura for x in pacientes_guerrero_negro]
    df['indice_de_masa_corporal'] = [ x.indice_de_masa_corporal for x in pacientes_guerrero_negro]
    df['aumento_trigliceridos'] = [ x.aumento_trigliceridos for x in pacientes_guerrero_negro]
    df['aumento_colesterol_HDL'] = [ x.aumento_colesterol_HDL for x in pacientes_guerrero_negro]
    df['tension_arterial'] = [ x.tension_arterial for x in pacientes_guerrero_negro]
    df['medicacion_anti_hipertensiva'] = [ x.medicacion_anti_hipertensiva for x in pacientes_guerrero_negro]
    df['glicemia_ayunas'] = [ x.glicemia_ayunas for x in pacientes_guerrero_negro]
    df['antecedentes_diabetes'] = [ x.antecedentes_diabetes for x in pacientes_guerrero_negro]
    df['consentimiento_informado'] = [ x.consentimiento_informado for x in pacientes_guerrero_negro]
    df['curp'] = [ x.curp for x in pacientes_guerrero_negro]

    df.to_excel(f"Quimica_Sanguinea_Guerrero_Negro{datetime.datetime.now().date()}.xlsx")

    with open(f"Quimica_Sanguinea_Guerrero_Negro{datetime.datetime.now().date()}.xlsx", 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename={f"Quimica_Sanguinea_Guerrero_Negro{datetime.datetime.now().date()}.xlsx"}'
        return response


########################################################################################################################################################################################

def pacientes_Isla_Cedros_qs30(request):

    pacientes_guerrero_negro = PacienteInformacion.objects.filter(id__in = [ x.paciente.id for x in QS30.objects.all()], lugar_nacimiento = "Isla de Cedros", edad__isnull = False)

    pruebas = QS30.objects.filter(paciente__in = [ x.id for x in pacientes_guerrero_negro]).values()

    columnas_qs30 = [
    'paciente',
    'sexo',
    'Edad',
    'curp',
    'Lugar de Nacimiento',
    'medicion_cintura',
    'indice_de_masa_corporal',
    'aumento_trigliceridos',
    'aumento_colesterol_HDL',
    'tension_arterial' ,
    'medicacion_anti_hipertensiva',
    'glicemia_ayunas',
    'antecedentes_diabetes',
    'consentimiento_informado',

    #########################################
    'glucosa' ,
    'nitrOgeno_Ureico' ,
    'urea_serica' ,
    'creatinina' ,
    'colesterol_Total',
    'trigliceridos' ,
    'acido_Urico_Serico' ,
    'proteinas_Totales' ,
    'albumina_Serica' ,
    'globulina' ,
    'deshidrogenasa_Lactica' ,
    'transaminasa_Glutamico_Oxalacetica' ,
    'transaminasa_Glutamico_Piruvica' ,
    'fosfatasa_Alcalina' ,
    'gammaglutamil_Transpeptidasa' ,
    'sodio_Sérico' ,
    'potasio_Sérico' ,
    'cloro_Serico' ,
    'calcio_Serico' ,
    'fosforo_Sérico' ,
    'bilirrubina_Total' ,
    'bilirrubina_Conjugada' ,
    'colesterol_alta_densidad' ,
    'colesterol_Baja_Densidad' ,
    'Indice_Aterogenico' ]

    df = pd.DataFrame(pruebas, index=None, columns=columnas_qs30)

    df['paciente'] = [ x.nombre_completo for x in pacientes_guerrero_negro]
    df['sexo'] = [ x.sexo for x in pacientes_guerrero_negro]
    df['Lugar de Nacimiento'] = [ x.lugar_nacimiento for x in pacientes_guerrero_negro]
    df['Edad'] = [ x.fecha_nacimiento for x in pacientes_guerrero_negro]
    df['medicion_cintura'] = [ x.medicion_cintura for x in pacientes_guerrero_negro]
    df['indice_de_masa_corporal'] = [ x.indice_de_masa_corporal for x in pacientes_guerrero_negro]
    df['aumento_trigliceridos'] = [ x.aumento_trigliceridos for x in pacientes_guerrero_negro]
    df['aumento_colesterol_HDL'] = [ x.aumento_colesterol_HDL for x in pacientes_guerrero_negro]
    df['tension_arterial'] = [ x.tension_arterial for x in pacientes_guerrero_negro]
    df['medicacion_anti_hipertensiva'] = [ x.medicacion_anti_hipertensiva for x in pacientes_guerrero_negro]
    df['glicemia_ayunas'] = [ x.glicemia_ayunas for x in pacientes_guerrero_negro]
    df['antecedentes_diabetes'] = [ x.antecedentes_diabetes for x in pacientes_guerrero_negro]
    df['consentimiento_informado'] = [ x.consentimiento_informado for x in pacientes_guerrero_negro]
    df['curp'] = [ x.curp for x in pacientes_guerrero_negro]


    df.to_excel(f"Quimica_Sanguinea_Isla_Cedros{datetime.datetime.now().date()}.xlsx")

    with open(f"Quimica_Sanguinea_Isla_Cedros{datetime.datetime.now().date()}.xlsx", 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename={f"Quimica_Sanguinea_Isla_Cedros{datetime.datetime.now().date()}.xlsx"}'
        return response


########################################################################################################################################################################################