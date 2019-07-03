# from ej_obj_her.PlazoFijo import *
# from ej_obj_her.CajaAhorro import *
from ej_obj_her.alumno_ej1 import *

# antonio = Cuenta()
# antonio.titular = "Pepe"
# antonio.cantidad = 100
# print(antonio.imprimir())

antonio = Alumno()

antonio.set_nombre(input("Dime el nombre: "))
antonio.set_nota(input("Dime su nota (entre 0 y 20): "))
print(antonio.aprobado())
