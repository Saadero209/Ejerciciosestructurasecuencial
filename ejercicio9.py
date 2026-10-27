#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
# martes 27 de noviembre de 2016

#Autor= Saad jlilou
#-----------------------
compra = float(input("digite la cantidad del compra: "))

descuento = compra * 0.15
pagar = compra - descuento

print("descuento:",descuento)
print("total pagar:",pagar)