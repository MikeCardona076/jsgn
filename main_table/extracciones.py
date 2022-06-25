from django.forms import model_to_dict
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
import openpyxl
import pandas as pd

from .serializers import *


########### Modelos ###############
from .Paciente.paciente_informacion import PacienteInformacion
from .master_table import EstudiosLaboratorio, PruebaLaboratorio



def get_guerreo_negro(request):
    pacientes_guerrero_negro =  PacienteInformacion.objects.filter(lugar_nacimiento = 'Guerrero Negro')

    serializer = PacienteInformacionSerializer(pacientes_guerrero_negro, many=True)


    df = pd.DataFrame(serializer.data)


    # df_gn =  dict()

    # for p in pacientes_guerrero_negro:

    #     if p.ficha not in df_gn:
    #         df_gn[p.ficha] = []

    #     df_gn[p.ficha].append(p.nombre_completo)
    #     df_gn[p.ficha].append(p.fecha_nacimiento)
    #     df_gn[p.ficha].append(p.sexo)
    #     df_gn[p.ficha].append(p.lugar_nacimiento)


    # df =  pd.DataFrame(df_gn)

    df.to_excel("Pacientes_Guerrero.xlsx")

 
    with open('Pacientes_Guerrero.xlsx', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Pacientes_Guerrero.xlsx"'
        return response


##############################################################################################################
def get_Islacedros(request):

    try:
        pacientes_isladecedros =  PacienteInformacion.objects.filter(lugar_nacimiento = 'Isla de Cedros')

        serializer = PacienteInformacionSerializer(pacientes_isladecedros, many=True)


        df = pd.DataFrame(serializer.data)

        # df_ic =  dict()

        # for p in pacientes_isladecedros:

        #     if p.id not in df_ic:
        #         df_ic[p.ficha] = []

        #     df_ic[p.ficha].append(p.nombre_completo)
        #     df_ic[p.ficha].append(p.fecha_nacimiento)
        #     df_ic[p.ficha].append(p.sexo)
        #     df_ic[p.ficha].append(p.lugar_nacimiento)
        #     df_ic[p.ficha].append(p.ficha)


        # df =  pd.DataFrame(df_ic)

        df.to_excel("Isladecedros.xlsx")
    
        with open('Isladecedros.xlsx', 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Isladecedros.xlsx"'
            return response

    except Exception as e:
        return HttpResponse(e)



##############################################################################################################

def get_quimica_sanguinea_all(request):
    
    try:
        pruebas_quimica_sanguinea =  PruebaLaboratorio.objects.filter(estudio = '1533')

        # Use the serializer to get the data in a dict format
        serializer = PruebaLaboratorioSerializer(pruebas_quimica_sanguinea, many=True)

        #Create a dataframe from the serializer data
        df = pd.DataFrame(serializer.data)

  


        #Rename the columns

      


        for row in df.iterrows():
            #Si hay un campo vacio, lo relleno con una cadena vacia
            if row[1]['unidad'] == '' or row[1]['unidad'] == None:
                df.at[row[0], 'unidad'] = 'N/A'

            if row[1]['estudio'] == '1533':
                df.at[row[0], 'estudio'] = 'Quimica Sanguinea 30'

        # fecha_nacimiento =  [x.fecha_nacimiento for x in PacienteInformacion.objects.all()]

        # df.insert(1, 'Fecha de Nacimiento', fecha_nacimiento)


       






            # if row[1]['prueba'] in [ x.clave for x in EstudiosLaboratorio.objects.all()]:
            #     df.at[row[0], 'prueba'] = EstudiosLaboratorio.objects.get(clave = row[1]['prueba']).nombre
            #     print(row[1]['prueba'])

        
        # columnas_qs30 = [ x.prueba for x in PruebaLaboratorio.objects.filter(estudio = '1533')]
        # #Eliminamos las columnas duplicadas
        # convert_list_to_set = set(columnas_qs30)
        
        # original_list = list(convert_list_to_set)

        # for e in EstudiosLaboratorio.objects.all():
        #     for p in original_list:
        #         if e.clave == p:
        #             original_list.remove(p)
        #             original_list.append(e.nombre)



        # columnas = ['paciente'] + original_list

        # # Llenamos la columna paciente PruebaLaboratorio.objects.filter(estudio = '1533')

        # df =  pd.DataFrame(columns=columnas)



        # df['paciente'] = [x.paciente for x in PruebaLaboratorio.objects.filter(estudio = '1533').order_by('paciente')]

        # for e in EstudiosLaboratorio.objects.all():
        #     df[e.nombre] =  [x.resultado for x in PruebaLaboratorio.objects.filter(estudio = '1533').order_by('paciente')]



        # print(len(df['paciente']))

        #Eliminamos las columnas duplicadas
        # df["Fecha de Nacimiento"] = pd.Series([ x.fecha_nacimiento for x in PacienteInformacion.objects.filter(ficha__in =PruebaLaboratorio.objects.filter(estudio = '1533').order_by('paciente'))])




      


        # #LLenar las columnas de prueba con los valores de la base de datos

        # for p in PruebaLaboratorio.objects.filter(estudio = '1533'):
        #     df[p.prueba] = [x.resultado for x in PruebaLaboratorio.objects.filter(estudio = '1533', paciente__in  = df['paciente'])]



    




        # quimica_sanguinea = PruebaLaboratorio.objects.filter(estudio='1533')

        # for e in EstudiosLaboratorio.objects.all():
        #     for q in quimica_sanguinea:
                
        #         if q.prueba not in dict_quimica_sanguinea:
        #             dict_quimica_sanguinea[e.nombre] = []
        #             #add another column for the estudio
        #             dict_quimica_sanguinea["Paciente"] = []

        #         dict_quimica_sanguinea[e.nombre].append(q.resultado)
        #         dict_quimica_sanguinea[e.nombre].append(q.paciente)
        #         dict_quimica_sanguinea["Paciente"].append(q.paciente)



        #         df =  pd.DataFrame.from_dict(dict_quimica_sanguinea, orient='index')
        #         df = df.transpose()


        df.to_excel("Quimica_Sanguinea.xlsx")

        with open('Quimica_Sanguinea.xlsx', 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="Quimica_Sanguinea.xlsx"'
            return response


    except Exception as e:
        print(e)
        return HttpResponse("Problemas al obtener los datos")




