#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones. Ejercicio
# martes 27 de noviembre de 2016

#Autor= Saad jlilou
#-----------------------

Sueldo=float(input("introduce el sueldo: "))
venta1=float(input("introduce el venta1: "))
venta2=float(input("introduce el venta2: "))
venta3=float(input("introduce el venta3: "))

comision= (venta1+venta2+venta3)*10
total =Sueldo+comision

print("comision por la venas: ",comision)
print("total por la venta: ",total)