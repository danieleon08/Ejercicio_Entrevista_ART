import random

# Función 1: Generador de números aleatorios del 1 al 5.
def generador5():
    return random.randint(1, 5)

# Función 2: Generador de números aleatorios del 1 al 7 usando generador5.
def generador7():
    while True:
        # 1. Se crea un generador de números aleatorios del 1 al 25 uniformemente distribuidos, usando dos llamadas a generador5
        resultado = 5 * (generador5() - 1) + generador5()
        
        # 2. Queremos que apartir de este generador5, podamos crear uno de 7.
        # Para esto, necesitamos números del 1 al 21 (porque 21 es el múltiplo de 7, es el más cercano a 25).
        # Esto lo hacemos obteniendo el resultado del paso anterior y verificando si es menor o igual a 21.
        # Asi ignoramos los números del 22 al 25, que no nos van servir para que el generador sea uniforme.

        if resultado <= 21:
            # 3. Obtenemos el numero del 1 al 7 a partir del resultado del paso anterior, usando la operación módulo.
            # El resultado será (resultado % 7) + 1
            # Con esto nos aseguramos de que el resultado sea un número entre 1 y 7, y que cada número tenga la misma probabilidad de aparecer.
            return (resultado - 1) % 7 + 1
        
            # Ejemplo:
            # Si resultado es 1, 8 o 15; el código devuelve 1.
            # Si resultado es 7, 14 o 21; el código devuelve 7.
        


# Aplicacion y prueba del generador7
estadisticas = {i: 0 for i in range(1, 8)}
for _ in range(2000):
    estadisticas[generador7()] += 1

print("Distribución tras 2,000 intentos:")
for num, freq in estadisticas.items():
    print(f"Número {num}: {freq} veces ({(freq/2000)*100:.2f}%)")