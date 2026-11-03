#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
# martes 3 de noviembre de 2026

#Autor= Saad jlilou

d = float(input("distancia entre los vehiculos: "))
v1 = float(input("velocidad del vehiculo atras: "))
v2 = float(input("velocidad del vehiculo delante: "))

t_horas = d / (v1-v2)
t_min = t_horas * 60
print(t_min)