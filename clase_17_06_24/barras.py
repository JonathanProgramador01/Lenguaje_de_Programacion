###### ESTA DE AQUII ES LA ENCARGAADA DE MIS BARAS
from turtle import *

class Barras:
    def __init__(self,direccion_inicial):
        self.barra = Turtle(shape="square")
        self.barra.shapesize(stretch_wid=1, stretch_len=6)
        self.barra.speed(0)
        self.barra.penup()
        self.barra.setheading(90)
        self.barra.color("#00ADB5")
        self.barra.goto(x=direccion_inicial, y=0)
    def arriva(self):

        if self.barra.ycor() <= 200:
            self.barra.forward(20)

    def abajo(self):
        if self.barra.ycor() >= -210:
            self.barra.backward(20)

