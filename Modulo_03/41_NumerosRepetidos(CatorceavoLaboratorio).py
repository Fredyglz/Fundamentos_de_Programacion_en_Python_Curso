miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
auxLista = []

for i in miLista:
    if i not in auxLista:
        auxLista.append(i)

miLista = auxLista[:]
print("La lista solo con elementos únicos:")
print(miLista)
