# Concatenacion y Replica
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# Demostrando la función ord ()
ch1 = 'a' 
ch2 = ' ' # espacio
ch3 = 'α'
ch4 = 'ę'

print(ord(ch1))
print(ord(ch2))
print(ord(ch3))
print(ord(ch4))

# Demostrando la función chr()
print(chr(97))
print(chr(945))

# Demonstrando min() 
print(min("aAbByYzZ"))

t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demostrando max() 
print(max("aAbByYzZ"))

t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrando el método index()
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demostrando la función list()
print(list("abcabc"))

# Demostrando el método count()
print("abcabc".count("b"))
print('abcabc'.count("d"))