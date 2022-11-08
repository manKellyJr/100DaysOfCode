"""Dice Roller by, Obed Banda
Simulate dice rolls using the Dungeons & Dragons dice roll notation.
View the code below
Tags: short, simulation"""

import random, sys

print('''Dice Roller, by Obed Banda

Enter what kind and how many dice to roll. The format is the number 
of dice, followed by "d", followed by the number of sides the dice have.
You can also a plus or minus adjustment.

Examples:
    3d6 rolls three 6-sided dice
    1d10+2 rolls one 10-sided die, and adds 2
    2d38-1 rolls two 38-sided, die and subtracts 1
    QUIT quits the program
''')

while True: # Main program loop:
    try:
        diceStr = input('> ')   # The prompt to enter the dice string.
        if diceStr.upper() == 'QUIT':
            print('Thanks for playiung!')
            sys.exit()

        # clean up the dice string:
        diceStr = diceStr.lower().replace(' ', '')

        # Find the 'd' in the dice string input
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')

        # Get the number of dice. (The "3" in "3d6+1"
        numberOfDice = diceStr[:dIndex]

