# Author Vladimir SR
"""
1.	El alumnado tendrá que realizar un programa que conste de
una clase llamada Alumno que tenga como atributos el nombre y
la nota del alumno. Definir los métodos para inicializar sus
atributos, imprimirlos y mostrar un mensaje con el resultado
de la nota y si ha aprobado o no.
"""


class Alumno(object):
    nombre = ""
    nota = 0

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, name):
        if str(name).isalnum() and name != "":
            self.nombre = name

    def get_nota(self):
        return str(self.nota) + " la nota va desde 0 hasta 20"

    def set_nota(self, score):
        if str(score).isdigit() and 0 <= int(score) <= 20:
            self.nota = score

    def aprobado(self):
        texto = "El alumno está "
        if self.nota >= 10:
            texto = texto + "APROBADO con un "
            if 10 <= self.nota < 13:
                texto = texto + "SUFICIENTE "
            if 13 <= self.nota < 16:
                texto = texto + "NOTABLE "
            if 16 <= self.nota <= 19:
                texto = texto + "SOBRESALIENTE "
            if self.nota == 20:
                texto = texto + "MATRÍCULA DE HONOR "
            texto = texto + "(" + str(self.nota) + " sobre 20)"
        else:
            texto = texto + "SUSPENDIDO con un "
            if 7 <= self.nota < 10:
                texto = texto + "NECESITA MEJORAR "
            if 4 <= self.nota < 7:
                texto = texto + "DEFICIENTE "
            if 1 <= self.nota <= 4:
                texto = texto + "MUY DEFICIENTE "
            if self.nota == 0:
                texto = texto + "CERO PATATERO "
            texto = texto + "(" + str(self.nota) + " sobre 20)"
        return texto
