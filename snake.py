import turtle
from turtle import Turtle

STARTINGSQUARES = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTINGSQUARES:
            self.addsegment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(10)

    def moveup(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.move()

    def movedown(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.move()

    def moveleft(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.move()

    def moveright(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.move()

    def addsegment(self,position):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.addsegment(self.segments[-1].position())







