class Empleado(object):
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario =salario
    def getnombre(self):
        return self.__nombre
    def getsalario(self):
        return self.__salario
    def setnombre(self,nombre):
        self._nombre = nombre
    def setsalario(self,salario):
        self.__salario =salario
    def delnombre(self):
        del self._nombre
    def delsalario(self):
        del self.__salario