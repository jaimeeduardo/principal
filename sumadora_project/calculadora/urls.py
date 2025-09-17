"""Rutas de la aplicación Calculadora."""
from django.urls import path

from . import views

app_name = "calculadora"

urlpatterns = [
    path("", views.sumar, name="sumar"),
]
