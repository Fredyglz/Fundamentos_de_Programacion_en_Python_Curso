def lbakg(lb):
    return lb * 0.45359237
    
def piepulgam(pie, pulgada = 0.0):
    return pie * 0.3048 + pulgada * 0.0254

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

print(imc(352.5, 1.65))
print(lbakg(1))
print(piepulgam(1,1))
print(piepulgam(6,1))
print(piepulgam(6))
#######################
print(imc(peso = lbakg(176), altura = piepulgam(5,7)))