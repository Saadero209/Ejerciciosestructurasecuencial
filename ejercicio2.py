#Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Introduce la base del rectangulo: "))
altura = float(input("Introduce la altura del rectangulo: "))

perimetro = 2 * (base + altura)
area = base * altura

print(f"El perimetro del rectangulo es: {perimetro}")
print(f"El area del rectangulo es: {area}")