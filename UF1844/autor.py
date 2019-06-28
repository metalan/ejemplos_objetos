# Author Vladimir SR
from datetime import *


class Autor(object):
    nombre = ""
    apellidos = ""
    identificador = 0
    nacimiento = date(1970, 1, 1)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        if nombre != "" and str(nombre).isalpha():
            self.nombre = nombre
        else:
            print("Nombre no valido")

    def get_apellidos(self):
        return self.apellidos

    def set_apellidos(self, apellido):
        if apellido != "" and str(apellido).isalpha():
            self.apellidos = apellido
        else:
            print("Apellido no valido")

    def get_identificador(self):
        return self.identificador

    def set_identificador(self, id):
        if id != 0 and str(id).isdigit():
            self.identificador = id
        else:
            print("Identificador no valido")

    def get_nacimiento(self):
        return self.nacimiento

    def set_nacimiento(self, nacimiento):
        pass
