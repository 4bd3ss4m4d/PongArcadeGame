# Scoreboard Class

from turtle import Turtle

FONTNAME = "Courier"
FONTSIZE = 15
FONTTYPE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 0)

    ''' PROVIDE PLAYER's name and alignment: "center', "left" or "right" and a tuple of coordinates (x, y).'''
    def update_scoreboard(self, player_name, alignment, coordinates):
        self.clear()
        self.goto(coordinates[0], coordinates[1])
        self.write(f"{player_name}\'s score: {self.score}", align=alignment, font=(FONTNAME, FONTSIZE, FONTTYPE))
        self.penup()

    def increase_score(self):
        self.score += 1
