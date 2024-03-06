num1 = float(input("Ingrese el primer número:"))2
num2 = float(input("Ingrese el segundo número:"))
num3 = float(input("Ingrese el tercer número:"))


if num1 != num2 and num1 != num3 and num3 != num2:
    if num1 <  num2 and num1 < num3:
        menor = num1

    elif num2 < num1  and  num1 < num3:
       menor = num2

    else:
        menor = num3

    print (f"El menor valor es: {menor}")
else:
    print("los tres valores deben ser diferentes, intenta nuevamente")

print("La suma de los tres números es", (num1+num2+num3))





