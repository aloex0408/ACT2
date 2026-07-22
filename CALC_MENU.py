while True:
    print("\n¿Deseas ingresar a la calculadora?")
    print("1. Sí")
    print("2. No")
    entrada = input("Elige una opción: ")
    if entrada == '2':
        print("Saliendo...")
        break
    if entrada != '1':
        print("Opción inválida")
        continue
    print("\n1. Sumar  2. Restar  3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '3':
        print("Saliendo...")
        break
    if opcion == '1':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Resultado:", a + b)
    elif opcion == '2':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print("Resultado:", a - b)
    else:
        print("Error: número inválido")