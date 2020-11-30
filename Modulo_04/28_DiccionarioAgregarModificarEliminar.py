dict = {"gato" : "perro", "perro" : "chien", "caballo" : "cheval"}
print(dict)

dict['gato'] = 'minou'
print(dict)

dict['cisne'] = 'cygne'
print(dict)

dict.update({"pato" : "canard"})
print(dict)

del dict['perro']
print(dict)

dict.popitem()
print(dict)