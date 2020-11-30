# Ejercicio 1
print("Ejercicio 1")
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
        
# Ejercicio 2
print("\nEjercicio 2")
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
    
# Ejercicio 3
print("\nEjercicio 3")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "")
    
# Ejercicio 4
print("\n\nEjercicio 4")
for digit in "0165031806510":
    if digit == "0":
        print("x", end = "")
        continue
    print(digit, end = "")
    