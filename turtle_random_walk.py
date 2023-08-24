import turtle
from turtle import Turtle, Screen
import random

my_t = Turtle()
my_t.shape("turtle")
my_t.pensize(10)
turtle.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b


random_numbers = [0,90,180,270,360]
random_number = [10,15,20,25,30,35]
my_t.speed(0)

for i in range(0,100):
    my_t.setheading(random.choice(random_numbers))
    my_t.forward(random.choice(random_number))
    my_t.color(random_colour())

screen = Screen()

screen.mainloop()