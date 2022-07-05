from django.db import models

# •	Fechas de la jornada de salud
# •	Características de la báscula (electrónica, mecánica, marca)
# •	Características de estadimetro (unidades de medida, limite máximo)
# •	Cinta métrica (unidades de medida, limite máximo)
# •	Características de baumanometro (digital, mercurio, marca)
# •	
# •	TOMA DE MUESTRA:
# •	Toma de muestras de sangre: ml extraídos de sangre, periodo de horas que tomaron las muestras (en de 8 a 9 am.) y las fechas,  tubos utilizados  (marcas).
# •	Características del equipo de laboratorio utilizado en el procesamiento de las muestras (marca, reactivos)

# class EquipoMedicion(models.Model):
#     fecha_jornada = models.DateField()
#     caracteristicas_bascula = models.CharField(max_length=100)
#     caracteristicas_estadimetro = models.CharField(max_length=100)
#     cinta_metrica = models.CharField(max_length=100)
#     caracteristicas_baumanometro = models.CharField(max_length=100)
#     toma_muestra = models.CharField(max_length=100)
#     caracteristicas_equipo_laboratorio = models.CharField(max_length=100)

#     def __str__(self):
#         return self.fecha_jornada

#     class Meta:
#         verbose_name = 'Equipo de medición'
#         verbose_name_plural = 'Equipos de medición'
#         ordering = ['fecha_jornada']
#         db_table = 'equipo_medicion'
#         managed = True
#         default_permissions = ()
#         permissions = (
#             ('list_equipo_medicion', 'Can list equipo medición'),
#             ('get_equipo_medicion', 'Can get equipo medición'),
#             ('create_equipo_medicion', 'Can create equipo medición'),
#             ('update_equipo_medicion', 'Can update equipo medición'),
#             ('delete_equipo_medicion', 'Can delete equipo medición'),
#         )
