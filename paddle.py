# Paddle Class

from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5, outline=1)
        self.goto(0, 0)
        self.color("white")

    def set_left_paddle(self):
        self.goto(-387, 0)

    def set_right_paddle(self):
        self.goto(379, 0)

    def up(self):
        # Stop the up() if it gets past a certain level
        if (self.xcor() == -387 and self.ycor() == (20*13)) or (self.xcor() == 379 and self.ycor() == (20*13)):
            pass
        else:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)

    def down(self):
        # Stop the down() if it gets past a certain level
        if (self.xcor() == -387 and self.ycor() == -1*(20*14)) or (self.xcor() == 379 and self.ycor() == -1*(20*14)):
            pass
        else:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)


