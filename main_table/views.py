from typing import Dict
from django.http import Http404
from django.shortcuts import render
from .Paciente.paciente_informacion import PacienteInformacion

from .master_table import *


# Create your views here.


def index(request):
    context = {
        'paciente': PacienteInformacion.objects.all()
    }
    return render(request, 'startmin/pages/index.html', context)



def guerreronegro(request):
    context = {
        'paciente': PacienteInformacion.objects.filter(lugar_nacimiento='Guerrero Negro')
    }
    return render(request, 'startmin/tables.html', context)


def isladecedros(request):

    context = {
        'paciente': PacienteInformacion.objects.filter(lugar_nacimiento='Isla de Cedros')
    }
    return render(request, 'startmin/isladecedros.html', context)


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
