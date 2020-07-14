import random


class Die:
    def __init__(self):
        self.sides = 6

    def roll(self):
        return 1 + random.randrange(self.sides)

