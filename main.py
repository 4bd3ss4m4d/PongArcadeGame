# Pong Game

###
'''
Created by 4bd3ss4md
'''
###

from turtle import Screen, listen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def main():
    # Set screen
    screen = Screen()
    screen.setup(width=800, height=675)
    screen.bgcolor("black")
    screen.title("Pong Arcade Game")
    # Turn off the tracer so that nothing happening in the screen gets shown
    screen.tracer(0)

    # Set left racket
    left_paddle = Paddle()
    left_paddle.set_left_paddle()
    # Set right racket
    right_paddle = Paddle()
    right_paddle.set_right_paddle()

    # Set ball
    ball = Ball()

    # Set left scoreboard:
    left_scoreboard = Scoreboard()
    left_scoreboard.update_scoreboard("Player 1", "right", ((-387 + 235), 300))

    # Set left scoreboard:
    right_scoreboard = Scoreboard()
    right_scoreboard.update_scoreboard("Player 2", "left", ((379 - 245), 300))

    # Listen to the screen
    listen()

    # Control left paddle
    screen.onkey(key="z", fun=left_paddle.up)
    screen.onkey(key="s", fun=left_paddle.down)
    # Control right paddle
    screen.onkey(key="Up", fun=right_paddle.up)
    screen.onkey(key="Down", fun=right_paddle.down)

    # Control The game
    game_status = True
    while game_status:
        # Update the screen
        ball.setheading(40)
        ball.move_ball()
        screen.update()

        # Detect collision with up or down wall
        if ball.ycor() >= 290 or ball.ycor() <= -280:
            ball.bounce_from_wall()

        # Detect collision with left paddle
        if ball.distance(left_paddle) <= 50 and ball.xcor() < (-387 + 20):
            ball.bounce_from_paddle()
            left_scoreboard.increase_score()
            left_scoreboard.update_scoreboard("Player 1", "right", ((-387 + 235), 300))

        # Detect collision with right paddle
        if ball.distance(right_paddle) <= 50 and ball.xcor() > (379 - 20):
            ball.bounce_from_paddle()
            right_scoreboard.increase_score()
            right_scoreboard.update_scoreboard("Player 2", "left", ((379 - 245), 300))

        # Detect when left paddle misses ball
        if ball.xcor() < -387 and ball.distance(left_paddle) > 50:
            ball.reset_ball()
            right_scoreboard.increase_score()
            right_scoreboard.update_scoreboard("Player 2", "left", ((379 - 245), 300))

        # Detect when right paddle misses ball
        if ball.xcor() > 379 and ball.distance(right_paddle) > 50:
            ball.reset_ball()
            left_scoreboard.increase_score()
            left_scoreboard.update_scoreboard("Player 1", "right", ((-387 + 235), 300))

    # Exit screen on click
    screen.exitonclick()


main()
