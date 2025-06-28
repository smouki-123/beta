import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    print(f"Lado 1: {dado1}")
    print(f"Lado 2: {dado2}")

    if dado1 % 2 == 0 and dado2 % 2 == 0:
        print(" YOU WIN ")
    else:
        print(" YOU LOUSE ")

lanzar_dados()
