from turtle import Turtle
class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.points}", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.points +=1
        self.update()

    def wallhit(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=("Arial", 32, "normal"))

