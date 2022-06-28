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

                'medicion_cintura',
                'indice_de_masa_corporal',
                'aumento_trigliceridos',
                'aumento_colesterol_HDL',
                'tension_arterial',
                'medicacion_anti_hipertensiva' ,
                'glicemia_ayunas' ,
        ]
        labels = {

                'nombre_completo': 'Nombre Completo',
                'fecha_nacimiento': 'Fecha de Nacimiento',
                'sexo': 'Sexo',
                'lugar_nacimiento': 'Lugar de Nacimiento',
                'ficha': 'Ficha',
                'medicion_cintura' : 'Medición de Cintura',
                'indice_de_masa_corporal' : 'Indice de Masa Corporal',
                'aumento_trigliceridos' : 'Aumento de Trigliceridos',
                'aumento_colesterol_HDL' : 'Aumento de Colesterol HDL',
                'tension_arterial' : 'Tensión Arterial',
                'medicacion_anti_hipertensiva' : 'Medicación Antihipertensiva',
                'glicemia_ayunas' : 'Glicemia Ayunas',
        }
        widgets = {
                'nombre_completo': forms.TextInput(attrs={'class':'form-control'}),
                'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),

                'sexo': forms.TextInput(attrs={'class':'form-control'}),


                'lugar_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
                'ficha': forms.TextInput(attrs={'class':'form-control'}),
                'medicion_cintura': forms.TextInput(attrs={'class':'form-control'}),
                'indice_de_masa_corporal': forms.TextInput(attrs={'class':'form-control'}),
                'aumento_trigliceridos': forms.TextInput(attrs={'class':'form-control'}),
                'aumento_colesterol_HDL': forms.TextInput(attrs={'class':'form-control'}),
                'tension_arterial': forms.TextInput(attrs={'class':'form-control'}),
                'medicacion_anti_hipertensiva' : forms.TextInput(attrs={'class':'form-control'}),
                'glicemia_ayunas' : forms.TextInput(attrs={'class':'form-control'}),
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