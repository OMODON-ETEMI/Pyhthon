from turtle import Turtle

# Define constants for the game.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []  # List to store the snake's segments.
        self.create_snake()  # Create the initial snake.
        self.head = self.segments[0]  # Reference to the snake's head.

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Create and add segments to the snake.

    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a new segment as a Turtle object.
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)  # Add the segment to the list.

    def extend(self):
        self.add_segment(self.segments[-1].position())  # Extend the snake by adding a new segment.

    def move(self):
        # Move the snake by updating the position of each segment.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward.

    def up(self):
        # Change the snake's direction to UP, but only if it's not currently moving DOWN.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to DOWN, but only if it's not currently moving UP.
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the snake's direction to LEFT, but only if it's not currently moving RIGHT.
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the snake's direction to RIGHT, but only if it's not currently moving LEFT.
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)