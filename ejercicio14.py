#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
# martes 3 de noviembre de 2026

#Autor= Saad jlilou

num = int(input("digite un numero: "))

cifra1= num // 10
cifra2= num % 10

invertido= cifra2 * 10 + cifra1

print(invertido)