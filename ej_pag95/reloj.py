# Author Vladimir SR
"""
Escribir una clase que represente un Reloj que señale la hora, el minuto y el segundo.
Podemos poner por defecto los parámetros a 0:0:0 o pasarle la hora, los minutos y los
segundos.
○ Los atributos serán tres enteros: para la hora, los minutos y los segundos.
○ Existirá un método que da la hora, que se llamará dame_hora() y la devolverá como
un objeto string.
○ La hora, los minutos y los segundos serán representados en todos los casos con
valores del tipo int. No obstante, se comprobarán los rangos adecuados (p.e. no
poner hora 35 horas).
"""


class Reloj(object):

    __horas = 0
    __minutos = 0
    __segundos = 0

    def dame_hora(self):
        return str(self.__horas) + ":" + str(self.__minutos) + ":" + str(self.__segundos)

    def __init__(self, hh, mm, ss):
        if hh.isdigit() and int(hh) < 24:
            self.__horas = hh
        if hh.isdigit() and int(mm) < 60:
            self.__minutos = mm
        if hh.isdigit() and int(ss) < 60:
            self.__segundos = ss