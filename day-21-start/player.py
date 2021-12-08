from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False











# 1 Create a turtle that starts at x = 0 and y at - 300
# 1.1 Turtle moves along the y axis 20 px at a time
# 1.3 When Turtle reaches y = 300, level Up, game restarts, cars move faster
# 1.4 If turtle is hit by car, game over.