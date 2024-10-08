from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
FORWARD=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    #Function to create a square shape turtle
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for positions in STARTING_POSITION:
            new_segement = Turtle("square")
            new_segement.color("light green")
            new_segement.penup()
            new_segement.goto(positions)
            self.segments.append(new_segement)

    def add_segment(self):
        new_segement = Turtle("square")
        new_segement.color("light green")
        new_segement.penup()
        last_segment=self.segments[-1]
        new_x = last_segment.xcor()
        new_y = last_segment.ycor()
        # Add a segment depending on the current direction of the snake's tail
        # We assume the snake moves in a straight line, so we add a segment behind
        if last_segment.heading() == UP:
            new_segement.goto(new_x, new_y - 20)
        elif last_segment.heading() == DOWN:
            new_segement.goto(new_x, new_y + 20)
        elif last_segment.heading() == LEFT:
            new_segement.goto(new_x + 20, new_y)
        elif last_segment.heading() == RIGHT:
            new_segement.goto(new_x - 20, new_y)
        self.segments.append(new_segement)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)


#遊戲規則，蛇不能掉頭
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
