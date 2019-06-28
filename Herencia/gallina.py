# Author Vladimir SR
from Herencia.oviparo import *


class Gallina(Oviparo):
    __huevos_puestos = 0

    def ponerHuevos(self):
        self.__huevos_puestos += 1

    def contarHuevos(self):
        return self.__huevos_puestos
