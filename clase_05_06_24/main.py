#Primer programaaa

print("#######PRIMER PROGRAMA ########")
velocidad = float(input("Introduce Velocidad: "))
tiempo = float(input("Introduce Tiempo: "))
print("Distancia Recorrida: ",round(tiempo*velocidad,2))

#Segundoo programaaa
print("\n#######SEGUNDO PROGRAMA ########")

ganados = int(input("Ingresaa cuantos partidos ganaste: "))
perdidos = int(input("Ingresaa cuantos partidos perdiste: "))
empatados = int(input("Ingresaa cuantos partidos empatados: "))

operacion = ganados *3
operacion += perdidos

print(f"Los puntos  que obtuvieste fueron: {operacion}")


#PITAGORASSSSS PROGRAMAAA

Ax = float(input("Ingresa Ax: "))
Ay = float(input("Ingresa Ay: "))
Bx = float(input("Ingresa Bx: "))
By = float(input("Ingresa By: "))

D = ((Ax-Bx)**2+(Ay-By)**2)**0.5

print(D)
