numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
numero3 = int(input("Ingresa el tercer numero: "))

nmasGrande = numero1

if numero2 > nmasGrande:
    nmasGrande = numero2
if numero3 > nmasGrande:
    nmasGrande = numero3
    
print("El numero mas grande es ", nmasGrande)