
precio_inicial = 1000


dia_semana = int(input("Ingresa el día de la semana (1: martes, 2: sábado, 3: feriado): "))


if dia_semana == 1:
    descuento = precio_inicial * 0.12
elif dia_semana == 2:
    descuento = precio_inicial * 0.18
elif dia_semana == 3:
    descuento = precio_inicial* 0.25
else:
    print("No sirve el día de la semana")



precio_descuento = precio_inicial - descuento


print(f"El cliente pagará ${precio_descuento:.2f} después del descuento.")
