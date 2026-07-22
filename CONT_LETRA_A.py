palabra = input("Ingresa una palabra: ")
# Convertimos a minúsculas para contar tanto 'A' como 'a'
cantidad = palabra.lower().count('a')
print("Cantidad de letras 'a':", cantidad)