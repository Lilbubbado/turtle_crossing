from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.set_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.set_up()

    def set_up(self):
        self.penup()
        self.hideturtle()
        self.goto(-275, 265)
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f'Game Over.', align="center", font=FONT)