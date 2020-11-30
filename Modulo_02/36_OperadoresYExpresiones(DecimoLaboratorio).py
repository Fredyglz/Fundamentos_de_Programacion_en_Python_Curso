hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
minutos = str((min + dura) % 60)
horas = str(((hora * 60 + min + dura) // 60) % 24)

print(horas + ":" + minutos)