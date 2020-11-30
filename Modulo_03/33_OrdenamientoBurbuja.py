miLista = [8, 10, 6, 2, 4] # Lista para ordenar
swapped = True # Lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # No hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True # Ocurrió el intercambio!  
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]
            
print(miLista)