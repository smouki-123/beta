import os
from random import randint

resultados = []
i = 1

while True:
    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"lanzamiento {i}:")
    print(f"dice : 1 {d1}")
    print(f"dice : 2 {d2}")
    print("\n")

    resultados.append((i, d1, d2))

    respuesta = input("desea continuar? (si/no:)")
    if respuesta.lower() == "si":
        i += 1
    elif respuesta.lower() == "no":
        print("Resumen de lanzamientos:")
        for resultado in resultados:
            print(f"Lanzamiento {resultado[0]}: Dado 1 = {resultado[1]}, Dado 2 = {resultado[2]}")
        print(f"\nTotal de lanzamientos: {len(resultados)}")
        break
    else:
        print("Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

