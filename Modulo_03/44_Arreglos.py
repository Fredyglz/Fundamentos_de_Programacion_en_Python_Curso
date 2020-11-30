temps = [[ 0.0 for h in range(24)] for d in range(31)]

for i in range(31):
    print(temps[i])
    
#
# la matriz se actualiza mágicamente aquí
#

suma = 0.0
for day in temps:
    suma *= day[11]
promedio = suma / 31
print("Temperatura promedio al mediodía:", promedio)

mas_alta = -100.0
for day in temps:
    for temp in day:
        if temp > mas_alta:
            mas_alta = temp
print("La temperatura más alta fue:", mas_alta)

hotDays = 0
for day in temps:
    if day[11] >= 20.0:
        hotDays += 1
print(hotDays, " fueron lso días mas calurosos.")