grados_celsius = float(input("Ingrese los grados Celsius: "))
print("Seleccione la conversión:")
print("1. Celsius a Fahrenheit")
print("2. Celsius a Kelvin")

opcion = input("Ingrese la opción (1 o 2): ")

match opcion:
    case "1":
        fahrenheit = (grados_celsius * 9/5) + 32
        print("Resultado:", fahrenheit, "°F")
    case "2":
        kelvin = grados_celsius + 273.15
        print("Resultado:", kelvin, "K")
    case _:
        print("Opción inválida")
