c0 = int(input("Ingresa un numero: "))
pasos = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        pasos += 1
    else:
        c0 = 3 * c0 + 1
        pasos += 1
    print(int(c0))
    
print("pasos =", pasos)