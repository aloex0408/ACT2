# Programa 3: Encontrar el mayor y el menor de una lista

entrada = input("Ingresa números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

mayor = max(numeros)
menor = min(numeros)

print("Lista ingresada:", numeros)
print("El mayor es:", mayor)
print("El menor es:", menor)
