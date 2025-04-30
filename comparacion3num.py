num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if(num1 == num2 == num3):
    print("Los tres números son iguales")
else:
    mayor = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")
