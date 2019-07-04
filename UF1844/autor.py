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
        if apellido != "":
            self.apellidos = apellido
        else:
            print("Apellido no valido")

    def get_identificador(self):
        return self.identificador

    def set_identificador(self, carnet):
        if id != 0 and str(carnet).isdigit():
            self.identificador = carnet
        else:
            print("Identificador no valido")

    def get_nacimiento(self):
        return self.nacimiento

    def set_nacimiento(self, year, month, day):
        ahora = date(datetime.now().year, datetime.now().month, datetime.now().day)
        fecha = date(1970, 1, 1)
        if str(year).isdigit() and int(year) > 0:
            if str(month).isdigit() and 1 < int(month) <= 12:
                if str(day).isdigit() and 1 < int(day) <= 31:
                    fecha = date(int(year), int(month), int(day))
                    if fecha < ahora:
                        self.nacimiento = fecha
                        return True
        return False
