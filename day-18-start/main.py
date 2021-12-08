import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()









# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))





































# =================Draw Shapes===================
# for shape in range(3, 10):
#     for i in range(shape):
#         tim.forward(100)
#         tim.left(360/shape)
#
# ========================Move turtle random and draw random colors==========================
#
# screen = Screen()
# screen.colormode(255)
#
#
# tim = Turtle()
# tim.shape("turtle")
# tim.pensize(10)
# tim.speed(10)
#
#
# def random_choice():
#     tim.pencolor()
#     angle = choice([-90, 90])
#     tim.right(angle)
#     distance = randint(50, 100)
#     tim.forward(distance)
#
# def color_of_movement():
#     tim.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#
#
# for i in range(0, 10000):
#     random_choice()
#     color_of_movement()




#
# tim = t.Turtle()
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
