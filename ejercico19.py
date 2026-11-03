#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
# martes 3 de noviembre de 2026

#Autor= Saad jlilou
correctas = int(input("Respuesta correcta: "))
incorrectos = int(input("Respuesta incorrectos: "))
blancas = int(input("Respuesta blancas: "))
nota = correctas *5 - incorrectos *1 + blancas *0
print(nota)
