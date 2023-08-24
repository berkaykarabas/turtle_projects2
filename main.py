from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("pink")
tim.speed(0)
colours = ["royal blue","forest green", "lawn green", "yellow", "moccasin", "deep pink", "seashell", "rosy brown", "blue violet", "ghost white", "slate blue", "dark green"]
def draw_shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        tim.forward(50)
        tim.right(angle)


for shape_side in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side)





screen = Screen()
screen.mainloop()