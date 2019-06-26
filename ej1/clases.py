# Author Vladimir SR
# Escribir una clase en python que convierta un número entero a número romano


class Romano(object):
    original = "0"
    __adaptados = [] # Privado
    __romanos = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # Privado

    def __init__(self): # Al crear
        pass

    def convertir(self, numero):
        self.original = str(numero)
        self.__convertir_original()
        print(str(self.__adaptados))

    def __convertir_original(self): #Privado
        self.__adaptados = list(self.original)
        for x in range(0, len(self.__adaptados)):
            self.__adaptados[x] = self.__romanos[int(self.__adaptados[x])]