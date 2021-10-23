# Ball Class

from time import sleep
from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.turtlesize(stretch_wid=1, stretch_len=1, outline=1)
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.movespeed = 0.08

    def move_ball(self):
        sleep(self.movespeed)
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_from_wall(self):
        self.move_y *= -1

    def bounce_from_paddle(self):
        self.move_x *= -1
        self.movespeed *= 0.95

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_from_paddle()
        self.movespeed = 0.08
