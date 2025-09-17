<?php

declare(strict_types=1);

/**
 * Suma dos números y devuelve el resultado.
 */
function sumar(float $primerNumero, float $segundoNumero): float
{
    return $primerNumero + $segundoNumero;
}

if (PHP_SAPI === 'cli') {
    if ($argc !== 3) {
        fwrite(STDERR, "Uso: php sumar.php <numero1> <numero2>\n");
        exit(1);
    }

    $numero1 = (float) $argv[1];
    $numero2 = (float) $argv[2];

    $resultado = sumar($numero1, $numero2);

    echo "La suma de {$numero1} y {$numero2} es {$resultado}\n";
}
