"""A Python turtle that does a random walk.

Author: Henrik Abel Christensen
"""
import random
from turtle import Screen
from typing import List

from argparser import parser
from tortoise import Tortoise


args = parser.parse_args()


def get_range(min_max: List[int]) -> range:
    """Returns a range with the turtles min max choices.

    If the input is None then range(-25, 26) is returned.

    Parameters
    ----------
    min_max : List[int]

    Returns
    -------
    min_max : range
    """
    if min_max is None:
        return range(-25, 26)
    minimum = min_max[0]
    maximum = min_max[1]
    if minimum == maximum:
        raise ValueError('min and max must be different')
    if minimum > maximum:
        raise ValueError('min must be lower than max')
    return range(minimum, maximum)


CHOICES = list(get_range(args.range))
MOVES = [(random.choice(CHOICES), random.choice(CHOICES)) for _ in range(args.steps)]

screen = Screen()
screen.mode('logo')  # <--- DO NOT CHANGE THIS!

t = Tortoise(visible=args.hide)

for move in MOVES:
    t.step(move)

screen.exitonclick()
