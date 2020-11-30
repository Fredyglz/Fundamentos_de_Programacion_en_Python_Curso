ingreso=float(input("Ingrese el ingreso anual: "))

if(ingreso < 85528):
    impuesto = (ingreso * .18) - 556.2
#elif(ingreso => 85.528):
else:
    impuesto = 14839.2 + ((ingreso - 85528) *.32)
    
if(impuesto < 0.0):
    impuesto = 0

impuesto=round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")
