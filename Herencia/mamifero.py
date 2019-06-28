# Author Vladimir SR
from Herencia.animal import *


class Mamifero(Animal):
    sangrecaliente = True

    def parir(self):
        return "Puedo parir"

    def amamantar(self):
        return "Puedo amamantar"
