# Ejemplo 01
cuadrados = [x ** 2 for x in range(10)]
dos = [2 ** i for i in range(8)]
probabilidades = [x for x in cuadrados if x % 2 != 0]

print(cuadrados)
print(dos)
print(probabilidades)