# Author Vladimir SR
from datetime import *


class Autor(object):
    """
    Los datos se manejan usando los gets y sets aunque las propiedades son públicas
    Los sets comprueban siempre la validez de los datos
    """
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
        # TODO Comprobar los días por meses
        # TODO Comprobar días de febrero
        # TODO Comprobar bisiestos
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

    def input_set_autor(self):
        """
        Esta función pide todos los datos al usuario
        :return: none
        """
        print("Datos del autor:")
        self.set_nombre(input("Pon un nombre:(alfanumérico)"))
        self.set_apellidos(input("Pon los apellidos:(alfanumérico)"))
        self.set_identificador(input("Pon el identificador:(numérico)"))
        print("Fecha de nacimiento:(todos numéricos)")
        self.set_nacimiento(input("Año:"), input("Mes:"), input("Día:"))

    def get_all(self):
        """
        Esta función devuelve una cadena de texto con todos los datos del libro
        :return: str
        """
        return "Datos del autor:\nNombre: " + self.get_nombre() + "\nApellidos: " + self.get_apellidos() + "\nIdentificador: " + str(self.get_identificador()) + "\nNacimiento: " + str(self.get_nacimiento())
