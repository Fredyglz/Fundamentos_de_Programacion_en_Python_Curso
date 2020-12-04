from sys import path

path.append('..\\paquetes')

# from extra.iota import funI
import extra.iota

# Llendo hasta el final del arbol del paquete
#import extra.good.best.sigma
import extra.good.best.sigma as sig
from extra.good.best.tau import funT
import extra.good.alpha as alp

print(extra.iota.funI())
print(extra.good.best.sigma.funS())
print(funT())
print(sig.funS())
print(alp.funA())