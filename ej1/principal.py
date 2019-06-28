from ej1.romanos import *
from ej1.Parentesis_ej3 import *
from ej1.potencia_ej3 import *

num = input("Introduce un número entero: ")
numero = Romano()

numero.convertir(num)


pepe = Parentesis()
print(pepe.comprobar_parentesis("()[]{}"))

print(pepe.comprobar_parentesis("([{}])"))

print(pepe.comprobar_parentesis("(]]()){}"))


eeuu = Potencia()

eeuu.elevar(2, 9)
