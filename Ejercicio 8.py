
print("Motos Honda =1000000$")
print("Moto Yamaha =800000$")
print("Moto Suzuki = 750000$")
print("Otra = 600000$")

precioM = float(input("Ingrese el precio de la moto:"))

Marca = float(input("Ingrese la marca de la moto:"))

if Marca == "Honda":
   descuento = precioM*0.05

elif Marca == "Yamaha":
    descuento = precioM*0.08

elif Marca == "Suzuki":
    descuento = precioM* 0.01

elif Marca == "Otra":
    descuento = precioM * 0.02

Precio_final = precioM- descuento

print(f"El precio de la moto es", precioM)
print(f"El descuento es de:", descuento)
print(f"El precio final de la moto es:", Precio_final)




