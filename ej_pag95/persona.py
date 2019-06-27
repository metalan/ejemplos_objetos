# Author Vladimir SR
"""
Crea una clase que se llame Persona, tendrá edad y nombre y podrá correr, saltar y
caminar. Crea a Esteban como objeto de la clase Persona y añadele las propiedades
correspondientes y los cuando llame a los métodos estos indicarán en una frase que
puede hacer (correr, saltar…).
"""


class Persona(object):
    __edad = 0
    __nombre = ""


    def correr(self):
        print("Puede correr")

    def saltar(self):
        print("Puede saltar")

    def caminar(self):
        print("Puede caminar")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def __init__(self, *args):
        self.__edad = args[0]
        self.__nombre = args[1]
