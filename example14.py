def solicitar_numeros():
    vector = []

    n = int(input("¿Cuántos números deseas ingresar? "))
    
    while len(vector) < n:
        nuevo = int(input(f"Ingrese el número #{len(vector)+1}: "))

        if len(vector) >= 2:
            suma = vector[-1] + vector[-2]
            while nuevo == suma:
                print(f"No se puede agregar {nuevo} porque es igual a la suma de los dos últimos valores ({vector[-2]} + {vector[-1]} = {suma})")
                nuevo = int(input("Ingrese otro número distinto: "))

        vector.append(nuevo)

    print("\nVector final:", vector)

solicitar_numeros()
