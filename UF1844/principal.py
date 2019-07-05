# Author Vladimir SR
from UF1844.libro import *
from UF1844.autor import *


class Principal(Libro, Autor):

    def __init__(self):
        pass

    def main(self):
        pepe = Autor()
        pepe.set_nombre("Antonio")
        pepe.set_apellidos("Pérez Guitierrez")
        pepe.set_identificador(151515)
        pepe.set_nacimiento(1990, 12, 15)
        print("Datos del autor:")
        print("Nombre: ", pepe.get_nombre())
        print("Apellidos: ", pepe.get_apellidos())
        print("Identificador: ", pepe.get_identificador())
        print("Nacimiento: ", pepe.get_nacimiento())

        carniboro = Libro("840102241X", "Largo pétalo de mar", 151515)
        print("Datos del libro:")
        print("Autor: ", carniboro.get_autor())
        print("ISBN: ", carniboro.get_isbn())
        print("Título: ", carniboro.get_titulo())

        carniboro.set_autor(1489757278755348919864622635181157)
        carniboro.set_titulo("El amante japonés")
        carniboro.set_isbn("9781101971642")
        carniboro.check_isbn(1515151515)
        print("Datos del libro:")
        print("Autor: ", carniboro.get_autor())
        print("ISBN: ", carniboro.get_isbn())
        print("Título: ", carniboro.get_titulo())


llamador = Principal()
llamador.main()
