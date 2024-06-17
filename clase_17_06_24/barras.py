###### ESTA DE AQUII ES LA ENCARGAADA DE MIS BARAS
from turtle import *

class Barras:
    def __init__(self,direccion_inicial):
        self.barra = Turtle(shape="square")
        self.barra.shapesize(stretch_wid=1, stretch_len=5)
        self.barra.speed(0)
        self.barra.penup()
        self.barra.setheading(90)
        self.barra.color("#76ABAE")
        self.barra.goto(x=direccion_inicial, y=0)
    def arriva(self):
        self.barra.forward(20)
    def abajo(self):
        self.barra.backward(20)
