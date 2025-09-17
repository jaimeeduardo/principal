"""Vistas de la aplicación Calculadora."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def sumar(request: HttpRequest) -> HttpResponse:
    """Muestra un formulario y calcula la suma de dos números."""

    resultado: float | None = None
    mensaje_error = ""
    numero_a = request.POST.get("numero_a", "")
    numero_b = request.POST.get("numero_b", "")

    if request.method == "POST":
        try:
            resultado = float(numero_a) + float(numero_b)
        except ValueError:
            mensaje_error = "Introduce valores numéricos válidos."
            resultado = None

    contexto = {
        "resultado": resultado,
        "mensaje_error": mensaje_error,
        "numero_a": numero_a,
        "numero_b": numero_b,
    }
    return render(request, "calculadora/index.html", contexto)
