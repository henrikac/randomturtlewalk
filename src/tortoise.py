"""A custom turtle.Turtle.

Author: Henrik Abel Christensen
"""
import turtle
from typing import Tuple


class Tortoise(turtle.Turtle):
    """Custom Turtle class.

    Parameters
    ----------
    shape : str
    visible : bool
    """
    def __init__(self, shape: str = 'turtle', visible: bool = True) -> None:
        super().__init__(shape=shape, visible=visible)

    def step(self, move: Tuple[int, int]) -> None:
        """Move the turtle forward.

        Parameters
        ----------
        move : Tuple[int, int]
            Delta x and delta y values.
        """
        delta_x, delta_y = move
        if delta_x < 0:
            self.setheading(270)
            self.backward(delta_x)
        elif delta_x > 0:
            self.setheading(90)
            self.forward(delta_x)
        if delta_y < 0:
            self.setheading(180)
            self.forward(delta_x)
        elif delta_y > 0:
            self.setheading(0)
            self.forward(delta_x)
