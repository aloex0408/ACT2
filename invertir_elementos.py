# Programa 4: Invertir elementos de una lista

entrada = input("Ingresa números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

invertida = numeros[::-1]

print("Lista ingresada:", numeros)
print("Lista invertida:", invertida)
