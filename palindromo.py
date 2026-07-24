texto = input("Ingresa una palabra o frase: ")

texto_sin_espacios = texto.replace(" ", "").lower()

if texto_sin_espacios == texto_sin_espacios[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
