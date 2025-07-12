'''''
generar una lista de numeros teniendo en cuenta un numero de incio (li) y un numero de fin (ls)
los numeros deben ser ingresados por el usuario

si el primer numero es mayor que el segundo la lista se debe imprimir en orden descendente.

'''''
import os
os.system('clear')

def generar_lista():
    li = int(input("Ingresa límite inferior: "))
    ls = int(input("Ingresa límite superior: "))
    if li <= ls:
        lista = list(range(li, ls + 1))
    else:
        lista = list(range(li, ls - 1, -1))
    print("La lista de números es:", lista)

generar_lista()