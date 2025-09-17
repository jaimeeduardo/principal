"""Modelos de dominio para la aplicación Calculadora."""
from django.db import models


class OperacionSuma(models.Model):
    """Representa una operación de suma almacenada en base de datos."""

    numero_a = models.FloatField("Primer número")
    numero_b = models.FloatField("Segundo número")
    resultado = models.FloatField("Resultado", editable=False)
    creado_en = models.DateTimeField("Registrado el", auto_now_add=True)

    class Meta:
        verbose_name = "operación de suma"
        verbose_name_plural = "operaciones de suma"
        ordering = ["-creado_en"]

    def save(self, *args, **kwargs):
        """Calcula el resultado antes de guardar la operación."""

        self.resultado = self.numero_a + self.numero_b
        super().save(*args, **kwargs)

    def __str__(self) -> str:  # pragma: no cover - representación sencilla
        return f"{self.numero_a} + {self.numero_b} = {self.resultado}"
