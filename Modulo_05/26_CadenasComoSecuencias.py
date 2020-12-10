# Indexando cadenas
exampleString = 'silly walks'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')
print()
for ix in range(len(exampleString)-1, -1, -1):
    print(exampleString[ix], end=' ')
print()

# Iterando a través de una cadena
for ch in exampleString:
    print(ch, end=' ')

# Rodajas o rebanadas
alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# Operadores in y not in
alpfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)

# Las cadenas de Python son inmutables
# Todo este codigo descomentado causara error
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Metodo del
# del alfabeto[0]

# Función append()
# alfabeto.append("A")

# Función insert()
# alfabeto.insert(0, "A")
