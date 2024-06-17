from turtle import Screen
from barras import Barras
from ball import Ball
import time

Window = Screen()
Window.setup(width=900, height=600)
Window.bgcolor("#222831")

Jugador1 = Barras(direccion_inicial=420)
Jugador2 = Barras(direccion_inicial=-420)
Ball = Ball()

Window.tracer(0)
juego_esta_activo = True

Window.onkey(Jugador1.arriva, "Up")
Window.onkey(Jugador1.abajo, "Down")
Window.onkey(Jugador2.arriva, "w")
Window.onkey(Jugador2.abajo, "s")
Window.listen()

ultimo_tiempo = time.time()

while juego_esta_activo:
    tiempo_actual = time.time()
    if tiempo_actual - ultimo_tiempo >= 0.3:
        Ball.move_ball()
        if Ball.pared():
            pass







        ultimo_tiempo = tiempo_actual

    Window.update()



