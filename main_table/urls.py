from django.urls import path
from . import views
from django.contrib.auth import views as login_views
from .extracciones import *



_ED = [

    path('get-guerreo-negro/', get_guerreo_negro, name='get_guerreo_negro'),
    path('get-Islacedros/', get_Islacedros, name='get_Islacedros'),
    path('get-get_quimica_sanguinea_all/', get_quimica_sanguinea_all, name='get_quimica_sanguinea_all'),
    path('actualizar_info/', views.actualizar_info, name='actualizar_info'),
    
]

urlpatterns = [
    path('', login_views.LoginView.as_view(template_name='dash/login.html'), name='login'),
    path('logout/', login_views.LogoutView.as_view(template_name='dash/login.html'), name='logout'),
    path('dashboard/', views.index, name='index'),
    path('guerreronegro/', views.guerreronegro, name='guerreronegro'),
    path('results/<str:ficha>/', views.results, name='results'),
    path('isladecedros/', views.isladecedros, name='isladecedros'),

    #Update
    path('paciente/<int:pk>/update/', views.PacienteUpdate.as_view(), name='paciente_update'),
] + _ED