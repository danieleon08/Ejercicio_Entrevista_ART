# Generador Uniforme 1-7 (Basado en 1-5)

Este proyecto implementa un algoritmo lógico para expandir un rango de aleatoriedad. El objetivo es construir un **generador de números aleatorios del 1 al 7** con distribución uniforme, utilizando como única fuente de aleatoriedad un generador de números del 1 al 5.

## 🚀 Estructura del Proyecto

El código se ha organizado de forma modular para seguir buenas prácticas de desarrollo:

* `generador5.py`: Contiene la función base `gen5()` que devuelve números del 1 al 5.
* `generador7.py`: Contiene la lógica principal del algoritmo de expansión.
* `main.py`: Script de ejecución para realizar las pruebas de uniformidad y estadísticas.

## 🧠 Explicación del Algoritmo

La solución se basa en tres pasos fundamentales, utilizando el método de **muestreo por rechazo**:

1.  **Creación de un Espacio Muestral Mayor (1-25):** Se crea un generador de números aleatorios del 1 al 25 uniformemente distribuidos, usando dos llamadas a `generador5`. La fórmula utilizada es:
    $$resultado = 5 \times (gen5() - 1) + gen5()$$

2.  **Filtrado para Uniformidad (Muestreo por Rechazo):**
    Para que el generador sea uniforme, necesitamos números del 1 al 21 (porque 21 es el múltiplo de 7 más cercano a 25). 
    * Si el resultado es **menor o igual a 21**, se acepta el número.
    * Se **ignoran los números del 22 al 25**, ya que no nos van a servir para que el generador sea uniforme.

3.  **Mapeo Final (Operación Módulo):**
    Obtenemos el número del 1 al 7 a partir del resultado aceptado en el paso anterior, usando la operación módulo:
    $$(resultado - 1) \pmod 7 + 1$$
    Con esto nos aseguramos de que el resultado sea un número entre 1 y 7, y que cada número tenga la misma probabilidad de aparecer. 

    * **Ejemplo:** * Si el resultado es 1, 8 o 15; el código devuelve **1**.
        * Si el resultado es 7, 14 o 21; el código devuelve **7**.

## 📊 Interpretación de Resultados

Al ejecutar el script de pruebas (`main.py`), se genera una tabla de frecuencias. Así es como se deben interpretar los datos:

* **Frecuencia Teórica:** El valor ideal es del **14.28%** ($100 / 7$). 
* **Uniformidad:** Si tras 2,000 intentos los porcentajes de cada número (1 al 7) son muy similares entre sí, confirmamos que el generador no tiene sesgos.
* **Confiabilidad:** El uso de un volumen alto de intentos permite que la distribución real se acerque a la probabilidad teórica, validando la lógica del algoritmo.

## 🛠️ Cómo ejecutar el proyecto

1.  Asegúrate de tener todos los archivos en la misma carpeta.
2.  Abre una terminal en esa ubicación.
3.  Ejecuta el archivo principal:
    ```bash
    python main.py
    ```
