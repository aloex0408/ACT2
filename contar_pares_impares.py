# Programa 1: Contar pares e impares

entrada = input("Ingresa números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

pares = sum(1 for n in numeros if n % 2 == 0)
impares = len(numeros) - pares

print("Lista ingresada:", numeros)
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
