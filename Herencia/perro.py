# Author Vladimir SR
from Herencia.mamifero import *


class Perro(Mamifero):
    colorPelo = ""

    def ladrar(self):
        return "Me gusta ladrar"

    def correr(self):
        return "Me gusta correr"