class Antena(object):
    color = ""
    longitud = ""

class Pelo(object):
    color = ""
    textura = ""

class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""

class Objeto(object):
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()

    def flotar(self):
        print(12)

class Dedo(object):
    longitud = ""
    forma = ""
    color = ""

class Pie(object):
    forma = ""
    color = ""
    dedos = 5

    def amputar(self):
        if self.dedos == 0:
            return "No hay dedos que cortar"
        self.dedos = self.dedos - 1
        return self.dedos

class NuevoObjeto(Objeto):
    pie = Pie()
    def saltar(self):
        print(21)

class Maquinas(object):
    maquina = 5

    def maquinas(self):
        self.maquina += 1
