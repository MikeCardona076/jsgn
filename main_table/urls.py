from django.urls import path
from . import views
from django.contrib.auth import views as login_views


urlpatterns = [
    path('', login_views.LoginView.as_view(template_name='startmin/pages/login.html'), name='login'),
    path('logout/', login_views.LogoutView.as_view(template_name='startmin/pages/login.html'), name='logout'),
    path('dashboard/', views.index, name='index'),
    path('guerreronegro/', views.guerreronegro, name='guerreronegro'),
    path('results/<str:ficha>/', views.results, name='results'),
    path('isladecedros/', views.isladecedros, name='isladecedros'),

    #Update
    path('paciente/<int:pk>/update/', views.PacienteUpdate.as_view(), name='paciente_update'),
]