# Author Vladimir SR
"""
2.	Desarrollar un programa que conste de una clase padre Cuenta
y dos subclases PlazoFijo y CajaAhorro. Definir los atributos
titular y cantidad y un método para imprimir los datos en la
clase Cuenta. La clase CajaAhorro tendrá un método para heredar
los datos y uno para mostrar la información.

La clase PlazoFijo tendrá dos atributos propios, plazo e interés.
Tendrá un método para obtener el importe del interés
(cantidad*interés/100) y otro método para mostrar la información,
datos del titular plazo, interés y total de interés.

Crear al menos un objeto de cada subclase.
"""
from ej_obj_her.Cuenta import *


class PlazoFijo(Cuenta):
    plazo = 0
    interes = 0

    def importe_interes(self):
        return self.cantidad * self.interes / 100

    def imprimir(self):
        return str(self.titular) + " tiene " + str(self.cantidad) + " 🐐"
