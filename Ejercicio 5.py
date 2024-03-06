print("Pecio de la camisa == 15000")

Ncamisas = float(input("Ingrese el número de camisas que compró:"))

if 3 >= Ncamisas:
    print("Obtienes un descuento del 20%, o sea", (Ncamisas*0.2*15000,"$"))

else:
    print("Obtienes un descuento del 10%, o sea", (Ncamisas*0.1*15000 ,"$"))