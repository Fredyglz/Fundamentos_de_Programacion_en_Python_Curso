EMPTY = "-"
TORRE = "TORRE"
PEON = "PEON"
CABALLO = "CABALLO"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)

tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE
tablero[4][2] = CABALLO

for i in range(8):
    tablero[1][i] = PEON
    tablero[6][i] = PEON

for i in range(8):
    print(tablero[i])
