from django.urls import path
from . import views
from django.contrib.auth import views as login_views
from .extracciones import *

from .extraccionv02 import *

new_extraccion = [
    path('extraccion-guerrero-negro/v02/', pacientes_guerrero_negro_qs30, name='pacientes_guerrero_negro_qs30'),
    path('pacientes-Isla-Cedros-qs30/v02/', pacientes_Isla_Cedros_qs30, name='pacientes_Isla_Cedros_qs30'),
]


_ED = [

    path('get-guerreo-negro/', get_guerreo_negro, name='get_guerreo_negro'),
    path('get-Islacedros/', get_Islacedros, name='get_Islacedros'),
    path('actualizar_info/', views.actualizar_info, name='actualizar_info'),

    
]

urlpatterns = [
    path('', login_views.LoginView.as_view(template_name='dash/login.html'), name='login'),
    path('logout/', login_views.LogoutView.as_view(template_name='dash/login.html'), name='logout'),
    path('dashboard/', views.index, name='index'),
    path('guerreronegro/', views.guerreronegro, name='guerreronegro'),
    path('results/<int:pk>/', views.results, name='results'),
    path('isladecedros/', views.isladecedros, name='isladecedros'),

    #Update
    path('paciente/<int:pk>/update/', views.PacienteUpdate.as_view(), name='paciente_update'),
    path('PruebaLaboratorioUpdate/<int:pk>/update/', views.PruebaLaboratorioUpdate.as_view(), name='PruebaLaboratorioUpdate'),
] + _ED + new_extraccion