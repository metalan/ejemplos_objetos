# Author Vladimir SR
from ej_pag95.persona import *
from ej_pag95.reloj import *

pepe = Persona(25, "Paco")

print(pepe.get_edad(), pepe.get_nombre())

juan = Reloj()

print(juan.dame_hora())

juan.set_hora(23, 44, 12)

print(juan.dame_hora())

juan.set_hora(55, 44, 12)

print(juan.dame_hora())