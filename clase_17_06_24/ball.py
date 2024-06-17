## Estaaa es la respondable de que se muevaaa mi pelotaaa
from turtle import *

class Ball:
    def __init__(self):
        self.ball = Turtle(shape="circle")
        self.ball.color("#EEEEEE")
        self.ball.setheading(22)
        self.ball.penup()
    def move_ball(self):
        self.ball.forward(20)

    def pared(self):
        if self.ball.xcor() > 420 or self.ball.xcor() < -420:
            return True
        if self.ball.ycor() > 260 or self.ball.ycor() < -260:
            return True

    def cambio_de_direccion(self):
        #self.ball.setheading(self.x)
        pass





