import random


niveles = {
    "1": 20,
    "2": 30,
    "3": 50,
    "4": 100
}


while True:
    jugadores = int(input("¿Cuántos jugadores van a jugar? (2-4): "))
    if 2 <= jugadores <= 4:
        break
    print("⚠️ El número debe ser entre 2 y 4.")


while True:
    print("\nSelecciona el nivel del tablero:")
    print("1. Básico (20 posiciones)")
    print("2. Intermedio (30 posiciones)")
    print("3. Avanzado (50 posiciones)")
    print("4. Experto (100 posiciones)")
    nivel = input("Ingresa el número de nivel (1-4): ")
    if nivel in niveles:
        meta = niveles[nivel]
        break
    print("⚠️ Selección inválida. Intenta nuevamente.")


posiciones = [0] * jugadores
pares_consecutivos = [0] * jugadores
ganador = None


while not ganador:
    for i in range(jugadores):
        print(f"\nTurno del jugador {i + 1}")
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f"🎲 Dados: {dado1} y {dado2}")
        movimiento = dado1 + dado2
        posiciones[i] += movimiento
        print(f"🏁 Nueva posición: {posiciones[i]}")

        # Verifica si obtuvo par
        if dado1 == dado2:
            pares_consecutivos[i] += 1
            print(f"🔥 ¡Par #{pares_consecutivos[i]} consecutivo!")
        else:
            pares_consecutivos[i] = 0

        # Condición especial: 3 pares consecutivos
        if pares_consecutivos[i] == 3:
            ganador = i
            print(f"🎉 ¡Jugador {i + 1} gana por tres pares consecutivos!")
            break

        # Condición normal: llegar a la meta
        if posiciones[i] >= meta:
            ganador = i
            print(f"🎉 ¡Jugador {i + 1} ha alcanzado la meta!")
            break

print(f"\n🏆 ¡Felicidades al Jugador {ganador + 1}! Has ganado la Carrera Numérica.")
