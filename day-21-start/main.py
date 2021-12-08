import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.go_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()












screen.exitonclick()
# 1 Create a turtle that starts at x = 0 and y at - 300
# 1.1 Turtle moves along the y axis 20 px at a time
# 1.3 When Turtle reaches y = 300, level Up, game restarts, cars move faster
# 1.4 If turtle is hit by car, game over.

# 2 Create car class.
# 2.1 Cars move along x axis from + 300 to - 300
# 2.2 If car hits turtle, game over

# 3 Detect collision
# 3.1 Detect collision of turtle with car
# 3.1.1 If collision with car, game over
# 3.2 Detect collision of turtle with wall
# 3.2.1 If collision with wall, level up

# 4 Keep score
# 4.1 If collision with wall, add 1 to level.











