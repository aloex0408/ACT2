# Programa 2: Suma de elementos de una lista

entrada = input("Ingresa números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

suma = sum(numeros)

print("Lista ingresada:", numeros)
print("La suma de los elementos es:", suma)
