"""Vistas de la aplicación Calculadora."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import OperacionSuma


def sumar(request: HttpRequest) -> HttpResponse:
    """Muestra un formulario, registra y calcula la suma de dos números."""

    resultado: float | None = None
    mensaje_error = ""
    numero_a = request.POST.get("numero_a", "")
    numero_b = request.POST.get("numero_b", "")

    if request.method == "POST":
        try:
            numero_a_float = float(numero_a)
            numero_b_float = float(numero_b)
        except ValueError:
            mensaje_error = "Introduce valores numéricos válidos."
        else:
            operacion = OperacionSuma(numero_a=numero_a_float, numero_b=numero_b_float)
            operacion.save()
            resultado = operacion.resultado

    operaciones_recientes = OperacionSuma.objects.all()[:10]

    contexto = {
        "resultado": resultado,
        "mensaje_error": mensaje_error,
        "numero_a": numero_a,
        "numero_b": numero_b,
        "operaciones": operaciones_recientes,
    }
    return render(request, "calculadora/index.html", contexto)
