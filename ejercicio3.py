#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

#martes 27 de octubre de 2026

#Autor=Saad Jlilou
""""""""
import math

Cateto1 = float(input("Ingrese el primer cateto: "))
Cateto2 = float(input("Ingrese el segundo cateto: "))

hipotenusa = math.hypot(Cateto1 ** 2 + Cateto2 ** 2)

print(f"El hipotenusa es: {hipotenusa}")
