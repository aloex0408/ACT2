print("Información sobre la serie de terror 'From'")
print("1. Artista")
print("2. Película")
print("3. Serie")
print("4. Género")
print("5. Año")
print("6. Sinopsis")

opcion = input("Ingrese el número de la opción: ")

match opcion:
    case "1":
        print("Artista principal: Harold Perrineau")
    case "2":
        print("Película relacionada: No aplica, es una serie")
    case "3":
        print("Serie: From")
    case "4":
        print("Género: Terror, misterio y suspenso")
    case "5":
        print("Año: 2022")
    case "6":
        print("Sinopsis: Un grupo de personas queda atrapado en un pueblo donde la noche trae criaturas peligrosas.")
    case _:
        print("Opción inválida")
