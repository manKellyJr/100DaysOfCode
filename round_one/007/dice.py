from random import randint


class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        landed_side = randint(1, self.sides)
        print("The die landed on {}".format(landed_side))

my_dice = Dice()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()