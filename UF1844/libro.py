# Author Vladimir SR


class Libro(object):
    """
    En esta clase usaremos los sets y gets para manejar los datos de Libros ya que son privados
    Los sets comprueban siempre la validez de los datos
    """
    __isbn = "7854123691"
    __titulo = "Título vacío"
    __autor = 0

    def __init__(self, isbn, titulo, autor):
        self.set_isbn(isbn)
        self.set_titulo(titulo)
        self.set_autor(autor)

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        if self.check_isbn(isbn):
            self.__isbn = isbn
        else:
            print("ISBN", isbn, "incorrecto, usando ISBN por defecto.")

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if titulo != "":
            self.__titulo = titulo
        else:
            print("Título no valido")

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        if autor != 0 and str(autor).isdigit():
            self.__autor = autor
        else:
            print("Autor no valido")

    def check_isbn(self, isbn):
        """
        FIXME Mejorar el código usando multiplicación de conjuntos:
        import operator
        lista = list(map(operator.mul, lista1, lista2))
        :param isbn: str
        :return: bool
        """
        if len(str(isbn)) == 10 or len(str(isbn)) == 13:
            lista = list(str(isbn))
            control_isbn = list(str(isbn))[len(str(isbn))-1]
            if len(str(isbn)) == 10:
                isbn10 = True
            else:
                isbn10 = False
            suma = 0
            control = ""
            if isbn10:
                for posicion in range(1, 10):
                    suma += int(lista[posicion-1]) * posicion
                control = str(suma % 11)
                if control == "10":
                    control = "X"
                if control_isbn == control:
                    return True
                else:
                    return False
            else:
                for posicion in range(0, 12):
                    if posicion % 2 == 0:
                        suma += int(lista[posicion])
                    else:
                        suma += int(lista[posicion]) * 3
                control = str((10 - suma) % 10)
                # resto = (10 - suma) % 10
                # if resto == 0:
                #     control = str(resto)
                # else:
                #     control = str(10 - resto)
                if control_isbn == control:
                    return True
                else:
                    return False
        else:
            return False

    def input_set_libro(self):
        """
        Esta función pide todos los datos al usuario
        :return: none
        """
        print("Datos del libro:")
        self.set_autor(input("Pon un autor:(numerico)"))
        self.set_isbn(input("Pon un isbn:(10 o 13)"))
        self.set_titulo(input("Pon un título:(alfanumérico)"))

    def get_all(self):
        """
        Esta función devuelve una cadena de texto con todos los datos del libro
        :return: str
        """
        return "Datos del libro:\nISBN: " + self.get_isbn() + "\nTITULO: " + self.get_titulo() + "\nAUTOR: " + str(
            self.get_autor())
