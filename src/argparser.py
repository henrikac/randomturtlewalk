"""ArgParser

Author: Henrik Abel Christensen
"""
import argparse


parser = argparse.ArgumentParser(description="Python turtle that does a random walk")

parser.add_argument("--hide", action="store_false",
                    help="sets the visible property of the turtle to false")
parser.add_argument("-r", "--range", nargs=2, type=int,
                    help="min and max value of the turtles choices")
parser.add_argument("-s", "--steps", type=int, default=100,
                    help="number of steps the turtle should take (default: 100)")
