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


class Cuenta(object):
    titular = ""
    cantidad = 0

    def imprimir(self):
        texto = str(self.titular) + " tiene " + str(self.cantidad) + " cabras\n"
        for cabras in range(0, self.cantidad):
            if cabras % 8 == 0:
                texto = texto + "\n"
            if cabras % 30 == 0 and cabras > 0:
                texto = texto + "\t\t\t🐕\n"
            texto = texto + "🐐"
        return texto
