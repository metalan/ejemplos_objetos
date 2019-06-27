from prueba_clases import *
from empleado import *
from factura import *

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

empleado1 = Empleado("Fancisco", 30000)
print(empleado1.getnombre())
empleado1.setnombre("Francisco jose")
print(empleado1.setnombre(), ",", empleado1.getsalario())

compra1 = Factura(12,110)
print(compra1.unidad)
print(compra1.precio)
print(compra1.a_pagar(),"euros")
print(Factura._tasas)
