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


def results(request, ficha):


    context = {
        'qs30_resultado': PruebaLaboratorio.objects.filter(paciente = ficha, estudio='1533'),
        'bh': PruebaLaboratorio.objects.filter(paciente = ficha, estudio='Biometria Hematica Completa'),
    }

    return render(request, 'Result/results.html', context)


class PacienteUpdate(UpdateView):
    model = PacienteInformacion
    form_class = PacienteInformacionForm
    template_name = 'Result/paciente_update.html'
    success_url = '/guerreronegro/'




def actualizar_info(request):
    try:
            pacientes = PacienteInformacion.objects.all()
            for paciente in pacientes:

                paciente.fecha_nacimiento = paciente.fecha_nacimiento[:10]
                paciente.save()

            ##################################################################
            pruebas = PruebaLaboratorio.objects.all()

            for prueba in pruebas:
                for paciente_info in pacientes:
                    if paciente_info.ficha == prueba.paciente:
                        prueba.nombre_paciente = paciente_info.nombre_completo
                        prueba.fecha_nacimiento = paciente_info.fecha_nacimiento
                        prueba.save()

            ##################################################################

            for e in EstudiosLaboratorio.objects.all():
                prueba_actualiza_nombre = PruebaLaboratorio.objects.all()
                for p in prueba_actualiza_nombre:
                    if p.prueba == e.clave:
                        p.prueba = e.nombre
                        p.save()

            return redirect('/dashboard/')

            ##################################################################

    except Exception as e:
        print(e)
        return HttpResponse('Error al actualizar, intente de nuevo más tarde')
        


