# Author Vladimir SR
# Escribir una clase en python que convierta un número entero a número romano


class Romano(object):
    original = "0"
    __romanos = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    __romanos2 = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]  # Privado para sustituir
    __adaptados = [] # Privado
    __convertidos = [] # Privado

    def __init__(self): # Al crear
        pass

    def sustituir(self, numero):
        self.original = str(numero)
        self.__sustitucion_romana()
        print(str(self.__adaptados))

    def convertir(self, numero):
        self.original = str(numero)
        self.__conversion_romana()
        print(str(self.__convertidos))

    def __sustitucion_romana(self): #Privado
        self.__adaptados = list(self.original)
        for x in range(0, len(self.__adaptados)):
            self.__adaptados[x] = self.__romanos2[int(self.__adaptados[x])]+

    def __conversion_romana(self): #Privado
        pass