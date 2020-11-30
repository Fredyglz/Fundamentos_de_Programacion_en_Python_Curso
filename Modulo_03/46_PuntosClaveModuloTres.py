# Ejemplo 01
cubos = [num ** 3 for num in range (5)]
print(cubos) # salidas: [0, 1, 8, 27, 64]

# Ejemplo 02
# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

tabla = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(tabla)
print(tabla[0][0]) # salida: ':('
print(tabla[0][3]) # salida: ':)'

# Ejemplo 03
# Cubo - un arreglo tridimensional (3x3x3)

cubo = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cubo)
print(cubo[0][0][0]) # salida: ':('
print(cubo[2][2][0]) # salida: ':)'