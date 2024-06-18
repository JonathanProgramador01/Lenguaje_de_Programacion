from turtle import Screen
from barras import Barras
from ball import Ball
from lineas import Backgroud
from score import Score


import time

Window = Screen()
Window.setup(width=1200, height=600)
Window.title("Ping Pong")
Window.bgcolor("#222831")

Jugador1 = Barras(direccion_inicial=570)
Jugador2 = Barras(direccion_inicial=-577)

Backgroud = Backgroud()
Ball = Ball()
Score = Score()



Window.onkey(Jugador1.arriva, "Up")
Window.onkey(Jugador1.abajo, "Down")
Window.onkey(Jugador2.arriva, "w")
Window.onkey(Jugador2.abajo, "s")
Window.listen()



Window.tracer(0)
juego_esta_activo = True
ultimo_tiempo = time.time()
ultimo_tiempo2 = time.time()
velocidad = 0.3

while juego_esta_activo:
    tiempo_actual = time.time()
    if tiempo_actual - ultimo_tiempo >= velocidad:

        Ball.move_ball()

        if Ball.distancia(Jugador1.barra, Jugador2.barra):
            Ball.cambio_de_direccion_de_x()
        if Ball.pared_de_y():
            Ball.cambiar_direccion_de_y()

        if Ball.pared_de_x_del_jugador1():
            velocidad = 0.3
            Ball.start()
            Score.punto_jugador2()

        if Ball.pared_de_x_del_jugador2():
            velocidad = 0.3
            Score.punto_jugador1()
            Ball.start()

        ultimo_tiempo = tiempo_actual



    if tiempo_actual - ultimo_tiempo2 >= 0.5:
        if velocidad <= 0.01:
            velocidad = 0.01
        else:
            velocidad -= 0.00161
        ultimo_tiempo2 = tiempo_actual














    Window.update()



