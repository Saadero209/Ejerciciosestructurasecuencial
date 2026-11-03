#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
# martes 3 de noviembre de 2026

#Autor= Saad jlilou

HH = int(input("Introduzca la hora : "))
MM = int(input("Introduzca los minutos :"))
SS = int(input("Introduzca los segundo  :"))
T = int(input("Introduzca la tiempo del viaje :"))

total = HH * 3600 + MM * 60 + SS + T
print(total // 3600, "horas:" , total % 3600, "min:" , total % 60, "segundos:")