import turtle
import random

jared = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0, 90, 180, 270]
jared.pensize(15)
jared.speed("fastest")

for shape_side in range(500):
    jared.color(random_color())
    jared.forward(30)
    jared.setheading(random.choice(directions))