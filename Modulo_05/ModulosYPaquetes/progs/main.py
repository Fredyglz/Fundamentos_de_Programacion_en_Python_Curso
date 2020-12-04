# Si el modulo se ecnuentra el otro directorio, utlizar path
from sys import path
path.append('..\\modulos')
# path.append('D:\\Documentos\\Trabajos Personales\\Python\\Pagina_FundamentosDeProgramacionConPython_PythonInstitute\\Modulo_05\\ModulosYPaquetes\\modulos')

from modulo import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))  