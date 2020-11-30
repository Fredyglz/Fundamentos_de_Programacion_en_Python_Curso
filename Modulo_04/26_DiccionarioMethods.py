dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])

for key in sorted(dict.keys()):
    print(key, "->", dict[key])