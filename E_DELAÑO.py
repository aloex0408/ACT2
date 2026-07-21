
m = int(input("Ingrese el número del mes (1-12): ").strip())
match m:
        case 12 | 1 | 2:
            print("Estación: Verano")
        case 3 | 4 | 5:
            print("Estación: Otoño")
        case 6 | 7 | 8:
            print("Estación: Invierno")
        case 9 | 10 | 11:
            print("Estación: Primavera")
        case _:
            print("Mes fuera de rango. Ingrese un número entre 1 y 12.")
