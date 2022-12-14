"""Carrot in a box by, Obed Banda
A silly bluffing game between two human players. Based on the game
from the show 8 Out of 10 Cats.

Tags: large, begginer, game, two-playesrs"""

import random

print('''Carrot in a Box, by Obed Banda

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.''')

input('Press Enter to begin...')

p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 1, enter your name: ')
playerNames = p1Name[:11].center(11) + '     ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES: 
   __________     __________
 /         / |   /         /|
 +---------+ |  +---------+ |
 |  RED    | |  |  GOLD   | |
 |  BOX    | /  |  BOX    | /
 +---------+/   +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLD box in front of you.')
print()
print(p1Name + ', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and don\'t look!!!')
input('When ' + p2Name + ' has closed their eyes, press Enter...')
print()

print(p1Name + 'here is the inside of your box: ')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
    ____VV____
    |   VV    |  
    |   VV    |
    |___||____|   __________
    /   ||   /|  / /|
    +---------+   | +---------+ |
    |   RED   | | | GOLD | |
    |   BOX   | / | BOX | /
    +---------+/ +---------+/
    ''')



print(p1Name + ' here is the inside of your box: ')