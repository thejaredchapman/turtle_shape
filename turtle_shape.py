import turtle
import random

jared = turtle.Turtle()

colors = ["red","orange","yellow","blue","indigo","violet","light blue","pink","brown"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        
        jared.forward(100)
        jared.right(angle)

for shape_side in range(3,15):
    jared.color(random.choice(colors))
    draw_shape(shape_side)