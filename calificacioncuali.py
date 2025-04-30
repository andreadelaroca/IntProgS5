#solicita una calificación númerica entre 0 y 100 y clasificala

calificacion = float(input("Ingrese su calificación: "))

if(0 <= calificacion <= 60):
    print("Reprobado")
elif(calificacion <= 70):
    print("Regular")
elif(calificacion <= 80):
    print("Bueno")
elif(calificacion <= 90):
    print("Muy bueno")
elif(calificacion <= 100):
    print("Excelente")
else:
    print("La calificación no es válida")
