while True:
    letra = input("Ingresa una letra (o presiona Espacio y Enter para salir): ").lower()
    
    if letra == " ":
        break
    
    if letra in "aeiou":
        print("Es una vocal")
    elif letra.isalpha():
        print("Es una consonante")