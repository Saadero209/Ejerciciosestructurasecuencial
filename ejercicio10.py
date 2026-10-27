#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:  55% del promedio de sus tres calificaciones parciales.  30% de la calificación del examen final.  15% de la calificación de un trabajo final.
# martes 27 de noviembre de 2016

#Autor= Saad jlilou
#-----------------------
p1 = int(input("digite primer valor: "))
p2 = int(input("digite segundo valor: "))
p3 = int(input("digite terceiro valor: "))
examen = float(input("examen: "))
trabajo = float(input("trabajo: "))

promedio = p1+p2+p3 /3
final = promedio * 0,55 + examen + trabajo * 0,15

print("final : ",final)