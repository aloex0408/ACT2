num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

a = num1
b = num2

while b != 0:
    a, b = b, a % b

print(f"El MCD de {num1} y {num2} es: {a}")
