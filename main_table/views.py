from cgi import print_arguments
import datetime
from typing import Dict
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .Paciente.paciente_informacion import PacienteInformacion

from .master_table import *

#Impor UpdateView
from django.views.generic import UpdateView


#Forms
from .forms import *

# Create your views here.


def index(request):


    context = {
        'pacientes_GN' : PacienteInformacion.objects.filter(lugar_nacimiento = 'Guerrero Negro').count(),
        'pacientes_IC'  : PacienteInformacion.objects.filter(lugar_nacimiento = 'Isla de Cedros').count(),
        'pacientes': PacienteInformacion.objects.all().count()
    }
    return render(request, 'dash/index.html', context)



def guerreronegro(request):

        
    context = {
        'paciente': PacienteInformacion.objects.filter(lugar_nacimiento='Guerrero Negro')
    }
    return render(request, 'dash/tables.html', context)


def isladecedros(request):

    context = {
        'paciente': PacienteInformacion.objects.filter(lugar_nacimiento='Isla de Cedros')
    }
    return render(request, 'dash/isladecedros.html', context)


def results(request, pk):
    context = {
        'bh': QS30.objects.filter(id=pk),
        'paciente': PacienteInformacion.objects.get(id=pk)
    }

    return render(request, 'Result/results.html', context)


class PacienteUpdate(UpdateView):
    model = PacienteInformacion
    form_class = PacienteInformacionForm
    template_name = 'Result/paciente_update.html'
    success_url = '/guerreronegro/'



def calcula_IMC(talla, peso):
    imc = eval(f'{peso} / ({talla} * {talla})')
    return round(imc, 2)


def actualizar_info(request):
    try:
        pacientes = PacienteInformacion.objects.all()
        for p in pacientes:
            if p.peso is not None and p.talla is not None:
                p.indice_de_masa_corporal = calcula_IMC(p.talla, p.peso)
                p.save()
                print('Actualizado')

        return redirect('/dashboard/')
    except Exception as e:
        print(e)
        return HttpResponse(e)
        



###########################################################

class PruebaLaboratorioUpdate(UpdateView):
    model = QS30
    form_class = QS30Form
    template_name = 'funciones/formulario.html'
    success_url = '/guerreronegro/'




        # pacientes = PacienteInformacion.objects.all()
        # pacientes_QS30 = QS30.objects.all()
        # for qs30 in pacientes_QS30:
        #     for paciente in pacientes:
        #         if paciente.id == qs30.paciente.id:
        #             paciente.glicemia_ayunas = qs30.glucosa
        #             paciente.aumento_colesterol_HDL =  qs30.colesterol_alta_densidad
        #             paciente.aumento_trigliceridos = qs30.trigliceridos
        #             paciente.save()
        #             print('Actualizado')
        #         else:
        #             print('No actualizado')


            # pacientes = PacienteInformacion.objects.all()
            # for paciente in pacientes:

            #     paciente.fecha_nacimiento = paciente.fecha_nacimiento[:10]
            #     paciente.save()

            # ##################################################################
            # pruebas = PruebaLaboratorio.objects.all()

            # for prueba in pruebas:
            #     for paciente_info in pacientes:
            #         if paciente_info.ficha == prueba.paciente:
            #             prueba.nombre_paciente = paciente_info.nombre_completo
            #             prueba.fecha_nacimiento = paciente_info.fecha_nacimiento
            #             prueba.save()

            # ##################################################################

            # for e in EstudiosLaboratorio.objects.all():
            #     prueba_actualiza_nombre = PruebaLaboratorio.objects.all()
            #     for p in prueba_actualiza_nombre:
            #         if p.prueba == e.clave:
            #             p.prueba = e.nombre
            #             p.save()
