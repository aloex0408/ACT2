parciales = float(input("Ingresa la calificación de parciales: "))
proyecto = float(input("Ingresa la calificación del proyecto: "))
examen = float(input("Ingresa la calificación del examen: "))
calificacion_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)
print("La calificación final es:", calificacion_final)
match True:
    case _ if calificacion_final >= 90:
        print("Excelente")
    case _ if calificacion_final >= 80:
        print("Muy bien")
    case _ if calificacion_final >= 70:
        print("Bien")
    case _ if calificacion_final >= 60:
        print("Suficiente")
    case _:
        print("Reprobado")
