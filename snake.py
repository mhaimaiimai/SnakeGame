from turtle import Turtle

STARTING_POSITION = [0,0]
SHAPE_SIZE = 1
MOVE_STEP = 20*SHAPE_SIZE
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self, num_segment=3):
        self.snake = []
        self.create_snake(num_segment)
        self.head = self.snake[0]
            
    def create_snake(self, num_segment=3):
        for n in range(num_segment):
            position = [STARTING_POSITION[0]-SHAPE_SIZE*20*n, STARTING_POSITION[1]]
            self.add_segment(position)
    
    def extend(self):
        position = [self.snake[-1].xcor(), self.snake[-1].ycor()]
        self.add_segment(position)
        
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.shapesize(SHAPE_SIZE)
        new_segment.penup()
        new_segment.setposition(x=position[0],y=position[1])
        self.snake.append(new_segment)
            
    def move(self):
        for n_square in range(len(self.snake)-1,0,-1):
            self.snake[n_square].setposition(self.snake[n_square-1].position())
        self.head.forward(MOVE_STEP)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def reset(self):
        for segment in self.snake:
            segment.hideturtle()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        