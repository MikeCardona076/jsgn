from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('', views.guerreronegro, name='guerreronegro'),
    path('results/<str:ficha>/', views.results, name='results'),
    path('isladecedros/', views.isladecedros, name='isladecedros'),
]