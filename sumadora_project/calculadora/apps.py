"""Configuración de la aplicación Calculadora."""
from django.apps import AppConfig


class CalculadoraConfig(AppConfig):
    """Configura la app calculadora."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "calculadora"
    verbose_name = "Calculadora"
