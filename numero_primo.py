numero = int(input("Ingresa un número: "))

if numero <= 1:
    print("No es primo")
else:
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
