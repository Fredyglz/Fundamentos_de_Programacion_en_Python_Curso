# lee tres numeros
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))

# verifica cual de los numeros es el mayor
# y pasalo a la variable de mayor numero
numeroMayor = max(numero1, numero2, numero3)

# verifica cual de los numeros es el mayor
# y pasalo a la variable de mayor numero
numeroMenor = min(numero1, numero2, numero3)

# imprime el resultado
print("El numero mas grande es: ", numeroMayor)
print("El numero mas chico es: ", numeroMenor)