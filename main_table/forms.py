from django import forms
from django.forms import ModelForm
from .master_table import *
from .Paciente.paciente_informacion import PacienteInformacion

from .Tablas.qs30 import QS30



class QS30Form(ModelForm):
    class Meta:
        model = QS30
        fields = "__all__"
        exclude = ['paciente']

        labels = {
                'glucosa': 'Glucosa',
                'nitrOgeno_Ureico': 'Nitrógeno Úrico',
                'urea_serica': 'Urea Sérica',
                'creatinina': 'Creatinina',
                'colesterol_Total': 'Colesterol Total',
                'trigliceridos': 'Trigliceridos',
                'acido_Urico_Serico': 'Ácido Urico Sérico',
                'proteinas_Totales': 'Proteinas Totales',
                'albumina_Serica': 'Albumina Sérica',
                'globulina': 'Globulina',
                'deshidrogenasa_Lactica': 'Deshidrogenasa Láctica',
                'transaminasa_Glutamico_Oxalacetica': 'Transaminasa Glutamico Oxalacetica',
                'transaminasa_Glutamico_Piruvica': 'Transaminasa Glutamico Piruvica',
                'fosfatasa_Alcalina': 'Fosfatasa Alcalina',

                'gammaglutamil_Transpeptidasa': 'Gammaglutamil Transpeptidasa',
                'sodio_Sérico': 'Sodio Sérico',
                'potasio_Sérico': 'Potasio Sérico',
                'cloro_Serico': 'Cloro Sérico',
                'calcio_Serico': 'Calcio Sérico',
                'fosforo_Sérico': 'Fosforo Sérico',
                'bilirrubina_Total': 'Bilirrubina Total',
                'bilirrubina_Conjugada': 'Bilirrubina Conjugada',
                'colesterol_alta_densidad': 'Colesterol Alta Densidad',
                'colesterol_Baja_Densidad': 'Colesterol Baja Densidad',
                'Indice_Aterogenico': 'Indice Aterogenico',
        }

        widgets = {
                'glucosa': forms.TextInput(attrs={'class': 'form-control'}),
                'nitrOgeno_Ureico': forms.TextInput(attrs={'class': 'form-control'}),
                'urea_serica': forms.TextInput(attrs={'class': 'form-control'}),
                'creatinina': forms.TextInput(attrs={'class': 'form-control'}),
                'colesterol_Total': forms.TextInput(attrs={'class': 'form-control'}),
                'trigliceridos': forms.TextInput(attrs={'class': 'form-control'}),
                'acido_Urico_Serico': forms.TextInput(attrs={'class': 'form-control'}),
                'proteinas_Totales': forms.TextInput(attrs={'class': 'form-control'}),
                'albumina_Serica': forms.TextInput(attrs={'class': 'form-control'}),
                'globulina': forms.TextInput(attrs={'class': 'form-control'}),
                'deshidrogenasa_Lactica': forms.TextInput(attrs={'class': 'form-control'}),
                'transaminasa_Glutamico_Oxalacetica': forms.TextInput(attrs={'class': 'form-control'}),
                'transaminasa_Glutamico_Piruvica': forms.TextInput(attrs={'class': 'form-control'}),
                'fosfatasa_Alcalina': forms.TextInput(attrs={'class': 'form-control'}),

                'gammaglutamil_Transpeptidasa': forms.TextInput(attrs={'class': 'form-control'}),
                'sodio_Sérico': forms.TextInput(attrs={'class': 'form-control'}),
                'potasio_Sérico': forms.TextInput(attrs={'class': 'form-control'}),
                'cloro_Serico': forms.TextInput(attrs={'class': 'form-control'}),
                'calcio_Serico': forms.TextInput(attrs={'class': 'form-control'}),
                'fosforo_Sérico': forms.TextInput(attrs={'class': 'form-control'}),
                'bilirrubina_Total': forms.TextInput(attrs={'class': 'form-control'}),
                'bilirrubina_Conjugada': forms.TextInput(attrs={'class': 'form-control'}),
                'colesterol_alta_densidad': forms.TextInput(attrs={'class': 'form-control'}),
                'colesterol_Baja_Densidad': forms.TextInput(attrs={'class': 'form-control'}),
                'Indice_Aterogenico': forms.TextInput(attrs={'class': 'form-control'}),
        }







# ##############################################################################################################
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
                'talla',
                'peso',
                'clasificacion_de_obesidad',
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
                'talla' : 'Talla',
                'peso' : 'Peso',
                'clasificacion_de_obesidad' : 'Clasificación de Obesidad',
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
                'talla' : forms.TextInput(attrs={'class':'form-control'}),
                'peso' : forms.TextInput(attrs={'class':'form-control'}),
                'clasificacion_de_obesidad' : forms.Select(attrs={'class':'form-control'}),
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