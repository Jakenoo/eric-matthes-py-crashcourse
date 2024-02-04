# 2/3/2024; exercise 9-13
# A short class simulating the roll of a die
from random import randint

class Die:
    """Rolling die simulator. You can adjust the number of sides the die has"""
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))

cube = Die(6)
icosahedron = Die(10)
dodecahedron = Die(20)

cube.roll_die()
icosahedron.roll_die()
dodecahedron.roll_die()