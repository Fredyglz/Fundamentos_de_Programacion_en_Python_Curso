# convencional

variable1 = 1
variable2 = 2

print("Variable1 =", variable1)
print("Variable2 =", variable2)

aux = variable1
variable1 = variable2
variable2 = aux

print("Variable1 =", variable1)
print("Variable2 =", variable2)

# python

variable1 = 1
variable2 = 2

print("Variable1 =", variable1)
print("Variable2 =", variable2)

variable1, variable2 = variable2, variable1

print("Variable1 =", variable1)
print("Variable2 =", variable2)