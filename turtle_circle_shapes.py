import turtle as t
from turtle import *
import random

my_t = t.Turtle()

t.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_random_colour = (r,g,b)
    return my_random_colour
my_t.speed(0)
circle_angle = random.randint(0,20)
for i in range(0,365,5):
    my_t.color(random_colour())
    my_t.circle(200)
    my_t.setheading(i)

screen = Screen()

screen.mainloop()