from prueba_clases import *

# et = Objeto()
# print(et.color)
# print(et.tamanio)
# print(et.aspecto)
# et.color = "rosa"
# print(et.color)

prueba = Objeto()

prueba.color = "verde"
prueba.aspecto = "feasco"

print(prueba.color, prueba.aspecto)

pepito = Pie()

pepito.dedos = 1
print(pepito.dedos)

pepito.amputar()
pepito.amputar()
print(pepito.dedos)

amputar = Pie()

amputar.dedos = 55
amputar.amputar()
print(amputar.dedos)

# Explicación del discurso de Mariano Rajoy
maquinas = Maquinas()
maquinas.maquina = 0
maquinas.maquinas()
maquinas.maquinas()

print("Maquinas:", maquinas.maquina)
