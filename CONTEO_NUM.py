cantidad = int(input("¿Cuántos números vas a ingresar?: "))
mayores = menores = ceros = 0

for _ in range(cantidad):
    num = int(input("Ingresa un número: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        ceros += 1

print(f"Mayores a cero: {mayores}, Menores a cero: {menores}, Iguales a cero: {ceros}")