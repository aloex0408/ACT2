suma = 0
contador = 0

while True:
    num = float(input("Ingresa un número positivo (negativo para salir): "))
    if num < 0:
        break
    suma += num
    contador += 1

if contador > 0:
    print("La media es:", suma / contador)
else:
    print("No se ingresaron números positivos.")