pesos_mexicanos = float(input("Ingrese la cantidad en pesos mexicanos: "))

print("Seleccione la moneda a convertir:")
print("1. USD")
print("2. EUR")
print("3. THB")
print("4. JPY")
print("5. KRW")
print("6. AUD")
print("7. PEN")
print("8. CAD")
print("9. VES")
print("10. ARS")

opcion = input("Ingrese el número de la opción: ")

match opcion:
    case "1":
        tasa = 17.00
        moneda = "USD"
    case "2":
        tasa = 18.50
        moneda = "EUR"
    case "3":
        tasa = 0.53
        moneda = "THB"
    case "4":
        tasa = 0.12
        moneda = "JPY"
    case "5":
        tasa = 0.012
        moneda = "KRW"
    case "6":
        tasa = 13.20
        moneda = "AUD"
    case "7":
        tasa = 4.60
        moneda = "PEN"
    case "8":
        tasa = 13.00
        moneda = "CAD"
    case "9":
        tasa = 0.0017
        moneda = "VES"
    case "10":
        tasa = 0.0085
        moneda = "ARS"
    case _:
        print("Opción inválida")
        raise SystemExit

resultado = pesos_mexicanos / tasa
print("Resultado:", round(resultado, 2), moneda)
