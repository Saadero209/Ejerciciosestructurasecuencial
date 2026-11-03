#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
# martes 3 de noviembre de 2026

#Autor= Saad jlilou
m2 = int(input("Introduzca m2: "))
m1 = int(input("Introduzca m1: "))
m50 = int(input("Introduzca m50: "))
m20 = int(input("Introduzca m20: "))
m10 = int(input("Introduzca m10: "))
total = m2 *200 + m1 *100 + m50 *50 + m20 *20 + m10 *10
print(total)
