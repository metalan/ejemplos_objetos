# Author Vladimir SR
from UF1844.libro import *
from UF1844.autor import *


class Principal(Libro, Autor):
    """
    Usamos la clase Principal para testear todas las funciones de las clases Autor y Libro
    Para evitar problemas, la función init de Principal redefine las heredadas
    """

    def __init__(self):
        pass

    def main(self):
        print("Comienzo de la sección automática:\n")
        pepe = Autor()
        pepe.set_nombre("Antonio")
        pepe.set_apellidos("Pérez Guitierrez")
        pepe.set_identificador(151515)
        pepe.set_nacimiento(1990, 12, 15)
        print(pepe.get_all())

        carniboro = Libro("840102241X", "Largo pétalo de mar", 151515)
        print(carniboro.get_all())

        carniboro.set_autor(1489757278755348919864622635181157)
        carniboro.set_titulo("El amante japonés")
        carniboro.set_isbn("9781101971642")
        carniboro.check_isbn(1515151515)
        print(carniboro.get_all())

        print("Comienzo de la sección manual:")
        seguir = True
        while seguir:
            carniboro.input_set_libro()
            carniboro.get_all()
            if input("¿Quieres seguir?:(s = Si)") != "s":
                seguir = False
            if not seguir:
                break
            else:
                pepe.input_set_autor()
                pepe.get_all()
                if input("¿Quieres volver a empezar?:(s = Si)") != "s":
                    seguir = False
