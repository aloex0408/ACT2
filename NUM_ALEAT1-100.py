import random

secreto = random.randint(1, 100)
adivina = 0

while adivina != secreto:
    adivina = int(input("Adivina el número (1-100): "))
    if adivina < secreto:
        print("Más alto")
    elif adivina > secreto:
        print("Más bajo")

print("¡Felicidades, adivinaste!")