#menu con las operaciones basicas
a = float(input("Introduzca un número: "))
b = float(input("Introduzca otro número: "))
print("Elija la operación a realizar: Suma (1), Resta (2), Multiplicación (3) y Divisón (4)")
operacion = int(input("Introduzca el número de la operación: "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
    
if(operacion == 1):
    print(f"El resultado es {suma}")
elif(operacion == 2):
    print(f"El resultado es {resta}")
elif(operacion == 3):
    print(f"El resultado es {multiplicacion}")
else:
    print(f"El resultado es {division}")
    