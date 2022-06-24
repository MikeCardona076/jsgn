from rest_framework import  serializers

########### Modelos ###############
from .Paciente.paciente_informacion import PacienteInformacion

from .master_table import EstudiosLaboratorio, PruebaLaboratorio


class PacienteInformacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PacienteInformacion
        fields = '__all__'

class PruebaLaboratorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PruebaLaboratorio
        fields = [
            'paciente',
            'nombre_paciente',
            'fecha_nacimiento',
            'estudio',
            'prueba',
            'resultado',
            'unidad',

        ]