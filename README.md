# Random Turtle Walk

Python turtle that takes a random walk.  

This project is inspired by [Wikipedia: Random walk](https://en.wikipedia.org/wiki/Random_walk).

## Requirements
+ Python 3.6+

## Installation
No installation is required to run the program.
However, to use `mypy` and `pylint` run

```terminal
pip install -r requirements.txt
```

*Note: It is recommended to create a virtual environment before running `pip install`.*

## Usage
To send the turtle on its random walk run `python src/main.py`.

#### Hide turtle
```terminal
python src/main.py --hide
```

#### Set number of steps
```terminal
python src/main.py -s 250
```
or
```terminal
python src/main.py --steps 250
```

#### Set the range of the turtles choices
```terminal
python src/main.py -r -10 10
```
or
```terminal
python src/main.py --range -10 10
```
