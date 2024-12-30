import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()

paint_needle_offset_Y = -20

start_needle_width = 250
needle_height_max = 85
needle_height_min = 70

trunk_height = 35
trunk_width = 10

min_snowflake_radius = 5
max_snowflake_radius = 10


def config_turtle(speed=10):
    t.ht()
    t.speed(speed)


def set_bg_color(bg_color="white"):
    screen.bgcolor(bg_color)


def set_pos(x=0, y=0):
    t.up()
    t.goto(x, y)
    t.down()


def rectangular(width, height):
    for i in range(2):
        t.forward(width)
        t.right(-90)
        t.forward(height)
        t.right(-90)


def paint_snowflake(count=10):
    t.color("white")
    for i in range(count):
        x = random.choice(range(-250, 250))
        y = random.choice(range(-250, 250))
        set_pos(x, y)
        t.begin_fill()
        rnd_radius = random.choice(range(min_snowflake_radius, max_snowflake_radius))
        t.circle(rnd_radius)
        t.end_fill()


def paint_present(x, y, width, height, color):
    t.color(color)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    rectangular(width, height)
    t.end_fill()


# region Tree
def random_needle_height():
    global needle_height_min
    global needle_height_max

    return random.choice(range(needle_height_min, needle_height_max))


def paint_trunk():
    t.color("brown")
    t.begin_fill()
    rectangular(trunk_width, trunk_height)
    t.end_fill()


def paint_needles(start_X, times):
    current_Y = t.ycor()
    current_Y += trunk_height

    t.color("green")

    needle_width = start_needle_width

    for i in range(times):
        start_paint_needle_X = start_X - needle_width / 2 + trunk_width / 2

        t.up()
        t.goto(start_paint_needle_X, current_Y)
        t.down()

        t.begin_fill()
        t.forward(needle_width)
        random_height = random_needle_height()
        t.goto(start_X + trunk_width / 2, current_Y + random_height)
        t.goto(start_paint_needle_X, current_Y)
        t.end_fill()

        current_Y += random_height + paint_needle_offset_Y
        needle_width /= 1.245


def paint_tree(start_X=0, start_Y=0, needle_counts=5, speed=10):
    set_pos(start_X, start_Y)
    paint_trunk()
    paint_needles(start_X, needle_counts)


# endregion

set_bg_color("cyan")

config_turtle()

paint_present(-75, -200, 50, 50, "red")
paint_present(-50, -215, 35, 35, "yellow")

paint_tree(-100, -200, 6)
paint_tree(150, -250, 5)
paint_snowflake(30)

# screen.mainloop()