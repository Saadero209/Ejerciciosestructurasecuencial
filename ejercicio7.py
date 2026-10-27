#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

# martes 27 de noviembre de 2016

#Autor= Saad jlilou
#-----------------------

minutos = int(input("introduce el numero de minutos: "))
horas = minutos // 60
mins = minutos % 60

print("minutos son :",minutos,"horas son :",horas,"mins : ", mins)