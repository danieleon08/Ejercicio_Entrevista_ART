from generador7 import gen7

# Aplicacion y prueba del generador7
estadisticas = {i: 0 for i in range(1, 8)}
# Generamos números usando gen7.
for _ in range(2000):
    estadisticas[gen7()] += 1

# Imprimimos la distribución de los números generados.
print("Distribución tras 2,000 intentos:")
for num, freq in estadisticas.items():
    print(f"Número {num}: {freq} veces ({(freq/2000)*100:.2f}%)")