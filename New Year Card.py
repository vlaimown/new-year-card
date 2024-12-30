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


def set_bg_color(bg_color = "white"):
  	screen.bgcolor(bg_color)


def reset_turtle(start_X = 0, start_Y = 0, speed = 10):
    t.ht()
    t.up()
    t.speed(speed)
    t.goto(start_X, start_Y)
    t.down()


def random_needle_height():
    global needle_height_min
    global needle_height_max

    return random.choice(range(needle_height_min, needle_height_max))


def paint_trunk():
    t.color("brown")
    t.begin_fill()

    for i in range(2):
        t.forward(trunk_width)
        t.right(-90)
        t.forward(trunk_height)
        t.right(-90)

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


def paint_tree(start_X = 0, start_Y = 0, needle_counts = 5, speed = 10):
    reset_turtle(start_X, start_Y, speed)
    paint_trunk()
    paint_needles(start_X, needle_counts)


set_bg_color("yellow")

paint_tree(-100, -200, 6)
paint_tree(100, -250, 5)

#screen.mainloop()