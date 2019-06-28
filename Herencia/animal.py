# Author Vladimir SR


class Animal(object):
    __peso = 0

    def comer(self):
        return None

    def set_peso(self, peso):
        if str(peso).isdigit():
            self.__peso = peso

    def get_peso(self):
        return self.__peso
