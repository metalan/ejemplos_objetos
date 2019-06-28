# Author Vladimir SR
from Herencia.delfin import *
from Herencia.gallina import *
from Herencia.perro import *

flipper = Delfin()


flipper.set_peso(1800)
print(flipper.nadar())

chueca = Gallina()
chueca.set_peso(1)
chueca.ponerHuevos()

toby = Perro()
print(toby.comer())
print(toby.ladrar())
print(toby.correr())

print(chueca.contarHuevos())
print(flipper.usar_pinguinos())