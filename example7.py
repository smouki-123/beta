'''''

script description
crea una script que lanze dos dados N veces y visualiza por pantalla los resultados.

la cantidad o numero de veces debe ser solicitada por el usiario.

deben lanzarce dos dados y usar funcion
'''''

import os
from random import randint

lan = int(input('cuantas veces deseas lanzar los dados'))


i = 1
while i <= lan:
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"lanzamiento {i}:")
    print(f"dice : 1 {d1}")
    print(f"dice : 2 {d2}")
    print("\n")

    i+=1