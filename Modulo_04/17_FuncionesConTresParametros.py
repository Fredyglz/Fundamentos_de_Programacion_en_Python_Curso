def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

def esUnTrianguloCompacta(a, b, c):
    if a + b <= c or b + c <= a or \
    c +a <= b:
        return False
    return True
    
def esUnTrianguloMasCompacta(a, b, c):
    return a + b > c and b + c > a and c + a > b 

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))
print(esUnTrianguloCompacta (1, 1, 1))
print(esUnTrianguloCompacta (1, 1, 3))
print(esUnTrianguloMasCompacta (1, 1, 1))
print(esUnTrianguloMasCompacta (1, 1, 3))
