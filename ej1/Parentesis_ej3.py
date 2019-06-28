# Author Vladimir SR
"""
Escribir una clase en python para encontrar la validez
de una cadena de paréntesis, '(', ')', '{', '}', '[' '].
Los paréntesis deben aparecer en el orden correcto, por
ejemplo "()" y "()[]{}" son válidos, pero "[)", "({[)]"
y "{{{" son inválidos.
"""

class Parentesis(object):
    cont_parentesis = 0
    cont_llaves = 0
    cont_corchetes = 0

    def __init__(self):
        print("Vamos a comprobar paréntesis")
