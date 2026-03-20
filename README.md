# Generador Uniforme 1-7 (Basado en 1-5)

El objetivo es construir un **generador de números aleatorios del 1 al 7** con distribución uniforme, utilizando como única fuente de aleatoriedad un generador de números del 1 al 5.

## Estructura del Proyecto

El código se ha organizado de forma modular para seguir buenas prácticas de desarrollo:

* `generador5.py`: Contiene la función base `gen5()` que devuelve números del 1 al 5.
* `generador7.py`: Contiene la lógica principal del algoritmo de expansión.
* `main.py`: Script de ejecución para realizar las pruebas de uniformidad y estadísticas.

## Explicación de la funcion gen7.

La solución se basa en tres pasos fundamentales, utilizando el método de **muestreo por rechazo**:

1.  Se crea un generador de números aleatorios del 1 al 25 uniformemente distribuidos, usando dos llamadas a `generador5`. La fórmula utilizada es:
    $$resultado = 5 \times (gen5() - 1) + gen5()$$

2.   ara que el generador sea uniforme, necesitamos números del 1 al 21 (porque 21 es el múltiplo de 7 más cercano a 25). 
    * Si el resultado es **menor o igual a 21**, se acepta el número.
    * Se **ignoran los números del 22 al 25**, ya que no nos van a servir para que el generador sea uniforme.

3.  Obtenemos el número del 1 al 7 a partir del resultado aceptado en el paso anterior, usando la operación módulo:
    $$(resultado - 1) \pmod 7 + 1$$
    Con esto nos aseguramos de que el resultado sea un número entre 1 y 7, y que cada número tenga la misma probabilidad de aparecer. 

    * **Ejemplo:**
        * Si el resultado es 1, 8 o 15; el código devuelve 1.
        * Si resultado es 2, 9 o 16; el código devuelve 2.
        * Si resultado es 3, 10 o 17; el código devuelve 3.
        * Si resultado es 4, 11 o 18; el código devuelve 4
        * Si resultado es 5, 12 o 19; el código devuelve 5.
        * Si resultado es 6, 13 o 20; el código devuelve 6
        * Si el resultado es 7, 14 o 21; el código devuelve 7.

## Pruebas

Al ejecutar el script de pruebas (`main.py`), se genera una tabla de frecuencias. Así es como se deben interpretar los datos.
En esta interpretacion se podra evidenciar si la distribucion es apropiada, esto pasa si el porcentaje de frecuencia de todos los numeros es muy parecida y cercana 14.28% (100/7)
Entre mayor sea las cantidad de números que genera, la probabilidad cumplira mejor estas condiciones.
## 🛠️ Cómo ejecutar el proyecto

1.  Asegúrate de tener todos los archivos en la misma carpeta.
2.  Abre una terminal en esa ubicación.
3.  Ejecuta el archivo principal:
    ```bash
    python main.py
    ```
