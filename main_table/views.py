import datetime
from typing import Dict
from django.http import Http404
from django.shortcuts import render
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
    # pacientes = PacienteInformacion.objects.all()

    # for paciente in pacientes:

    #     paciente.fecha_nacimiento = paciente.fecha_nacimiento[:10]
    #     paciente.save()
    #     print(f"Paciente Actualizado con exito por {request.user}")
        
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

    qs30_resultado = dict()

    for prueba in PruebaLaboratorio.objects.filter(paciente = ficha,estudio='1533'):
        for estudio in EstudiosLaboratorio.objects.all():
            if estudio.clave == prueba.prueba:
                # llave del diciconario es el nombre de la prueba y los valores son prueba.resultado y prueba.unidad
                qs30_resultado[estudio.nombre] = [prueba.resultado, prueba.unidad]
            else:
                continue

    context = {
        'qs30_resultado': qs30_resultado,
    }

    return render(request, 'Result/results.html', context)


class PacienteUpdate(UpdateView):
    model = PacienteInformacion
    form_class = PacienteInformacionForm
    template_name = 'Result/paciente_update.html'
    success_url = '/guerreronegro/'