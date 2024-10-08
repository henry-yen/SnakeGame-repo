from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write("Score: "+str(self.score),align="center",font=("Futura",30,"bold"))

    def add(self):
        self.score=self.score+1
        self.clear()
        self.write("Score: " + str(self.score), align="center", font=("Futura", 30, "bold"))

    def game_over(self):
        self.goto(0, -50)
        self.write("GAME OVER", align="center", font=("Futura", 80, "bold"))