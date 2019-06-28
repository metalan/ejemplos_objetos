# Author Vladimir SR


class Libro(object):
    __isbn = ""
    __titulo = ""
    __autor = 0

    def __init__(self, isbn, titulo, autor):
        pass

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        pass

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if titulo != "" and str(titulo).isalnum():
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
        if len(isbn) == 10 or len(isbn) == 13:
            lista = list(str(isbn))
            if len(isbn) == 10:
                isbn10 = True
                lista.insert(0, "0")
                lista.reverse()
            else:
                isbn10 = False
            suma = 0
            control = ""
            if isbn10:
                for posicion in range(len(lista) - 1):
                    suma += int(lista[posicion]) * posicion
                control = str(suma % 11)
                if control == "10":
                    control = "X"
                if lista[0] == control:
                    return True
                else:
                    return False
            else:
                for posicion in range(len(lista) - 1):
                    if posicion % 2 == 0:
                        suma += lista[posicion]
                    else:
                        suma += lista[posicion] * 3
                control = str(suma % 10)
                if lista[len(lista)] == control
                    return True
                else:
                    return False
        else:
            return False