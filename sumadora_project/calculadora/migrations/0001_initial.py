# Generated manually to introducir el modelo OperacionSuma
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OperacionSuma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero_a", models.FloatField(verbose_name="Primer número")),
                ("numero_b", models.FloatField(verbose_name="Segundo número")),
                (
                    "resultado",
                    models.FloatField(editable=False, verbose_name="Resultado"),
                ),
                (
                    "creado_en",
                    models.DateTimeField(auto_now_add=True, verbose_name="Registrado el"),
                ),
            ],
            options={
                "verbose_name": "operación de suma",
                "verbose_name_plural": "operaciones de suma",
                "ordering": ["-creado_en"],
            },
        ),
    ]
