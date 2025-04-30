a = float(input("Ingrese el primer lado: "))
b = float(input("Ingrese el segundo lado: "))
c = float(input("Ingrese el tercer lado: "))

if(a == b == c):
    print("El triángulo es equilátero")
elif(a == b or b == c or a == c):
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
