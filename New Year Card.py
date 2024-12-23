import turtle
import random

t = turtle.Turtle()
#sceen = turtle.Screen()

start_Y = -250
start_X = 0

current_X = start_X
current_Y = start_Y

paint_needle_offset_Y = -20

start_needle_width = 250
needle_height_max = 80
needle_height_min = 70

trunk_height = 35
trunk_width = 10

def reset(speed = 10):
  global start_X
  global start_Y
  
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
  global needle_height
  global current_X
  global current_Y
  
  t.up()
  t.goto(current_X, current_Y)
  t.down()
  
  t.color("brown")
  t.begin_fill()
  
  for i in range(2):
    t.forward(trunk_width)
    t.right(-90)
    t.forward(trunk_height)
    t.right(-90)
    
  t.end_fill()
  current_Y += trunk_height

def paint_needs(times):
  global current_X
  global current_Y
  global paint_need_offset_Y
  
  t.color("green")
  
  needle_width = start_needle_width
  
  for i in range(times):
    current_X = start_X - needle_width / 2 + trunk_width / 2
    
    t.up()
    t.goto(current_X, current_Y)
    t.down()
    
    t.begin_fill()
    t.forward(needle_width)
    random_height = random_needle_height()
    t.goto(start_X + trunk_width / 2, current_Y + random_height)
    t.goto(current_X, current_Y)
    t.end_fill()
    
    current_Y += random_height + paint_needle_offset_Y
    needle_width /= 1.225
    
reset()
paint_trunk()
paint_needs(7)

#screen.mainloop()