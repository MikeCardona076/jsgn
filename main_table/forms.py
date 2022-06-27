from django import forms
from django.forms import ModelForm
from .master_table import *
from .Paciente.paciente_informacion import PacienteInformacion



class PacienteInformacionForm(forms.ModelForm):
    
    class Meta:
        model = PacienteInformacion
        fields =[
                'nombre_completo',
                'fecha_nacimiento',
                'sexo',

                'lugar_nacimiento',
                'ficha',
        ]
        labels = {

                'nombre_completo': 'Nombre Completo',
                'fecha_nacimiento': 'Fecha de Nacimiento',
                'sexo': 'Sexo',

                'lugar_nacimiento': 'Lugar de Nacimiento',
                'ficha': 'Ficha',
        }
        widgets = {
                'nombre_completo': forms.TextInput(attrs={'class':'form-control'}),
                'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),

                'sexo': forms.TextInput(attrs={'class':'form-control'}),


                'lugar_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
                'ficha': forms.TextInput(attrs={'class':'form-control'}),
        }


    
#########################################################################################

class PruebaLaboratorioForm(forms.ModelForm):
    
    class Meta:
        model = PruebaLaboratorio
        fields =[
                'paciente',
                'nombre_paciente',
                'fecha_nacimiento',
                'prueba',
                'estudio',
                'resultado',
                'unidad',
        ]
        labels = {

                'paciente' : 'Paciente',
                'nombre_paciente' : 'Nombre Paciente',
                'fecha_nacimiento' : 'Fecha de Nacimiento',
                'prueba' : 'Prueba',
                'estudio' : 'Estudio',
                'resultado' : 'Resultado',
                'unidad' : 'Unidad',
        }
        widgets = {
                'paciente' : forms.TextInput(attrs={'class':'form-control'}),
                'nombre_paciente' : forms.TextInput(attrs={'class':'form-control'}),
                'fecha_nacimiento' : forms.TextInput(attrs={'class':'form-control'}),

                'prueba' : forms.TextInput(attrs={'class':'form-control'}),
                'estudio' : forms.TextInput(attrs={'class':'form-control'}),
                'resultado' : forms.TextInput(attrs={'class':'form-control'}),
                'unidad' : forms.TextInput(attrs={'class':'form-control'}),
        }