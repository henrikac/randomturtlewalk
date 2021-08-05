import random
from turtle import Screen

from tortoise import Tortoise


CHOICES = list(range(-25, 26))
MOVES = [(random.choice(CHOICES), random.choice(CHOICES)) for _ in range(1000)]

screen = Screen()
screen.mode('logo')

t = Tortoise()

for move in MOVES:
    t.step(move)

screen.exitonclick()
