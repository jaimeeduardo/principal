# Calculadora de suma con Django

Este repositorio incluye un proyecto mínimo de Django que permite calcular la suma de dos números a través de un formulario web.

## Requisitos

- Python 3.11 o superior
- [Django](https://www.djangoproject.com/) 4.x o superior (`pip install django`)

## Cómo ejecutar el proyecto

1. Crea y activa un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows usa: .venv\\Scripts\\activate
   ```

2. Instala las dependencias:

   ```bash
   pip install django
   ```

3. Ejecuta las migraciones iniciales:

   ```bash
   cd sumadora_project
   python manage.py migrate
   ```

4. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

5. Abre un navegador y visita `http://127.0.0.1:8000/` para acceder al formulario. Introduce dos números y pulsa **Sumar** para obtener el resultado.

## Estructura principal

- `sumadora_project/manage.py`: script de utilidades administrativas de Django.
- `sumadora_project/sumadora_project/`: configuración del proyecto.
- `sumadora_project/calculadora/`: aplicación que contiene la vista y las plantillas para realizar la suma.

## Pruebas

Puedes ejecutar las comprobaciones de Django con:

```bash
python manage.py check
```

Para crear tests automáticos puedes añadirlos en `sumadora_project/calculadora/tests.py`.
