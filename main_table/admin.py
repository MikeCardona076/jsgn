from atexit import register
import re
from django.contrib import admin

from main_table.Paciente.paciente_informacion import PacienteInformacion
from  .master_table import *
from django.dispatch import receiver

from import_export.signals import post_import


from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.core.exceptions import ObjectDoesNotExist

from .Tablas.qs30 import QS30






########################################################################################################################
class PacienteResource(resources.ModelResource):
    class Meta:
        model = PacienteInformacion

class PacienteAdmin(ImportExportModelAdmin):
        resource_class = PacienteResource
        search_fields = ['paciente__paciente__nombre', 'paciente__paciente__apellido']
        
        

admin.site.register(PacienteInformacion, PacienteAdmin)




########################################################################################################################
class PruebaLaboratorioResource(resources.ModelResource):

    class Meta:
        model = PruebaLaboratorio


    # def before_import(self, dataset, using_transactions=True, dry_run=False, **kwargs):

    #     for row in dataset.dict:


    #         if PacienteInformacion.objects.filter(ficha=row['paciente']).exists():
    #             paciente = PacienteInformacion.objects.filter(ficha=row['paciente'])[0]
    #             print("El paciente existe")
                
    #             print(f'Paciente: {row["paciente"]}')
    #             row['paciente'] = paciente.id
    #             print(f'Paciente:  x ID {paciente.id}')

    #         else:
    #             print(f'El paciente no existe {row["paciente"]}')
    #             #delete row
    #             dataset.dict.remove(row)
                

    #     # return super().before_import(dataset, using_transactions, dry_run, **kwargs)


class PruebaLaboratorioAdmin(ImportExportModelAdmin):
        resource_class = PruebaLaboratorioResource

    
        
        
        
admin.site.register(PruebaLaboratorio, PruebaLaboratorioAdmin)


########################################################################################################################
class EstudiosLaboratorioResource(resources.ModelResource):
    class Meta:
        model = EstudiosLaboratorio

class EstudiosLaboratorioAdmin(ImportExportModelAdmin):
        resource_class = EstudiosLaboratorioResource

        
        
        
admin.site.register(EstudiosLaboratorio, EstudiosLaboratorioAdmin)



#######################################
class QS30Resource(resources.ModelResource):
    class Meta:
        model = QS30

class QS30Admin(ImportExportModelAdmin):
        resource_class = QS30Resource

        

admin.site.register(QS30, QS30Admin)

