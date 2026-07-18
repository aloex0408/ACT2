s=float(input("Ingrese el salario bruto: "))
iva=0.16
d=float(input("Ingrese la deducción: "))
salario_neto=s-(s*iva)-d
print("El salario neto es:", salario_neto)
