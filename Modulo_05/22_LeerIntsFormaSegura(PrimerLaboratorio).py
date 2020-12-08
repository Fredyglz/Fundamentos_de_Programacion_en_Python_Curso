def readint(prompt, min, max):
    while True:
        try:
            n = int(input(prompt))
            assert n >= -10 and n <= 10
            return n
        except ValueError:
            print('Error: entrada incorrecta')
        except AssertionError:
            print('Error: el valor no está dentro del rango permitido (', min,'..',max,')')

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)