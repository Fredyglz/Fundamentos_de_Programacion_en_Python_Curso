miLista = [10, 1, 8, 3, 5]
print(miLista)

miLista[0], miLista[4] = miLista[4], miLista[0]
miLista[1], miLista[3] = miLista[3], miLista[1]

print(miLista)

# Con N numeros en la lista

miLista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(miLista)
longitud = len(miLista)

for i in range(longitud // 2):
    miLista[i], miLista[longitud - i - 1] = miLista[longitud - i - 1], miLista[i]
    
print(miLista)