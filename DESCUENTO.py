precio = float(input("Ingrese el precio del producto: "))
if precio <= 100:
    descuento = 0.05
elif precio <= 200:
    descuento = 0.10
elif precio <= 500:
    descuento = 0.15
else:
    descuento = 0.20
monto_descuento = precio * descuento
precio_final = precio - monto_descuento
print("Precio original:", precio)
print("Descuento aplicado:", descuento * 100, "%")
print("Monto del descuento:", monto_descuento)
print("Precio final:", precio_final)
