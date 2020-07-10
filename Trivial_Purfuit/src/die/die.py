import random


class Die:
    def __init__(self):
        self.sides = 6

    def roll(self):
        return 1 + random.randrange(self.sides)


def main():
    d1 = Die()
    for n in range(100):
        print(d1.roll())


main()
