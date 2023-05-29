from django.urls import path
from . import views

urlpatterns = [
    path('formulario_clase1/', views.formulario_clase1, name='formulario_clase1'),
    path('formulario_clase2/', views.formulario_clase2, name='formulario_clase2'),
    path('formulario_clase3/', views.formulario_clase3, name='formulario_clase3'),
]