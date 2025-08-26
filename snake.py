from turtle import Turtle
import time

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "stop"

    def create_snake(self):
        for i in range(3):
            self.add_segment((-20 * i, 0))

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].position())
        self.head.forward(20)

    def up(self): self.direction = "up" if self.direction != "down" else self.direction
    def down(self): self.direction = "down" if self.direction != "up" else self.direction
    def left(self): self.direction = "left" if self.direction != "right" else self.direction
    def right(self): self.direction = "right" if self.direction != "left" else self.direction

    def update_direction(self):
        if self.direction == "up": self.head.setheading(90)
        elif self.direction == "down": self.head.setheading(270)
        elif self.direction == "left": self.head.setheading(180)
        elif self.direction == "right": self.head.setheading(0)