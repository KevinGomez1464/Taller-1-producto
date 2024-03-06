Sueldo = float(input("Ingrese su sueldo:"))

if Sueldo <= 1000:
    print("Se descuenta 10% de tu salario",(Sueldo*0.1))
elif Sueldo <= 2000 and Sueldo <= 3000:
    print("Se descuenta un 5% adicional", (Sueldo*0.1*0.05))

elif Sueldo >= 3000:
    print("Se descuenta un 3% adicional",(Sueldo*0.1*0.05*0.03))