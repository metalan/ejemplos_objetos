# Author Vladimir SR
"""
Escribir una clase en python para encontrar la validez
de una cadena de paréntesis, '(', ')', '{', '}', '[' '].
Los paréntesis deben aparecer en el orden correcto, por
ejemplo "()" y "()[]{}" son válidos, pero "[)", "({[)]"
y "{{{" son inválidos.
"""

class Parentesis(object):
    def comprobar_parentesis(self, original):
        cont_parentesis = 0
        cont_llaves = 0
        cont_corchetes = 0
        comprobar = list(original)

        for check in comprobar:
            if check == "(":
                cont_parentesis += 1
            if check == ")":
                if cont_parentesis > 0:
                    cont_parentesis -= 1
                else:
                    return False
            if check == "{":
                cont_llaves += 1
            if check == "}":
                if cont_llaves > 0:
                    cont_llaves -= 1
                else:
                    return False
            if check == "[":
                cont_corchetes += 1
            if check == "]":
                if cont_corchetes > 0:
                    cont_corchetes -= 1
                else:
                    return False

        if cont_parentesis == 0 and cont_llaves == 0 and cont_corchetes == 0:
            return True
        else:
            return False