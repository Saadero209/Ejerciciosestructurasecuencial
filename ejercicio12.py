#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

# Jueves 29 de noviembre de 2026

#Autor= Saad jlilou

x1 = int(input("introduzca x1: "))
y1 = int(input("introduzca y1: "))
x2 = int(input("introduzca x2: "))
y2 = int(input("introduzca y2: "))

distanciax = x2 - x1
distanciay = y2 - y1

distamacia = (distanciax * distanciax + distanciay * distanciay) ** 0.5

print("La distancia es: ", distanciax + distanciay)