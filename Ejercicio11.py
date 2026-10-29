#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

# martes 27 de noviembre de 2026

#Autor= Saad jlilou

a = int(input("digite primer numero: "))
b = int(input("digite segundo numero: "))

if a > b:
    distancia = a - b
else:
    distancia = b - a

print("La distancia es: ", distancia)