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

jared.speed("fastest")

def draw_spiograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jared.color(random_color())
        jared.circle(100)
        jared.setheading(jared.heading() + size_of_gap)
        jared.circle(100)

draw_spiograph(5)


screen = turtle.Screen()
screen.exitonclick()