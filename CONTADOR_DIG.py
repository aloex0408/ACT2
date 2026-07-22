numero = int(input("Ingresa un número: "))
contador = 0

# Usamos un ciclo para dividir entre 10 y contar
while numero > 0:
    numero //= 10
    contador += 1

print("Cantidad de dígitos:", contador)