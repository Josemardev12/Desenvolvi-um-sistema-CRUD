from django.urls import path
from .views import *






urlpatterns = [
    path('', Home, name="home"),
    path('deleta/<int:id>/', deleta, name="deleta"),
    path('update/<int:id>/', actualizar, name="actualizar"),
    path('update/editar/', editar, name="editar"),
    path('adcionar/', adcionar, name="adcionar"),
    path('add/', add, name="add"),
]
