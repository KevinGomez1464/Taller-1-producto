
num1 = float(input("Ingrese el primer número:"))
num2 = float(input("Ingrese el segundo número:"))
num3 = float(input("Ingrese el tercer número:"))

if num1 != num2 and num1 != num3 and num3 != num2:
    if num1 > num2 and num1 > num3:
        mayor = num1

    elif num2 > num1  and  num1 > num3:
        mayor = num2

    else:
        mayor = num3

    print (f"El mayor valor es: {mayor}")
else:
    print("los tres valores deben ser diferentes, intenta nuevamente")




