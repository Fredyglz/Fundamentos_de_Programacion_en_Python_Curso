# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McMartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
newBeatles = ["Stu Sutcliffe", "Pete Best"]
for i in newBeatles:
    beatles.append(input("Agrega a " + i + " a la lista, nuevo miembro de la banda: "))
print("Paso 3:", beatles)

# etapa 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
