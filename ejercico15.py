#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuánto valen al final las dos variables.
# martes 3 de noviembre de 2026

#Autor= Saad jlilou

A=int(input("Introduzca A: "))
B=int(input("Introduzca B: "))

A, B = B, A
print("A:",A)
print("B:",B)