calificacion = str(input("Ingrese una letra de calificación (A, B, C, D, F): ").upper()
) 
if(calificacion == "A"):
    print("Excelente (90-100)")
elif(calificacion == "B"):
    print("Muy buena (80-89)")
elif(calificacion == "C"):
    print("Buena (70-79)")
elif(calificacion == "B"):
    print("Regular (60-69)")
elif(calificacion == "F"):
    print("Reprobado (0-59)")
else:
    print("Calificación no válida")
