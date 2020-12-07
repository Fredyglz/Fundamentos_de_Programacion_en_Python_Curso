def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

def banFun2(n):
    return 1 / n;

badFun(0)

try:
    banFun2(0)
except ArithmeticError:
    print('¿Que pasó? ¡Se lanzo una excepción!')

print("FIN.")