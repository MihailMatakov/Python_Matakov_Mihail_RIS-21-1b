
from pyDatalog import pyDatalog
import random
pyDatalog.create_terms('X, Y, y, Sm')
number=10

(y[X] == sum_(Y, for_each=Y)) <= ((Y._in(range_(X+1))))
print(f"{Sm == y[number]}")


