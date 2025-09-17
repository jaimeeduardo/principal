"""Puntos de entrada para las rutas principales del proyecto."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("calculadora.urls")),
]
