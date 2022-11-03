""" Blackjack, by Obed Banda obedbanda34@gmail.com
Thje classic card game also known as 21.

Tags: large, game, car game
"""

import random, sys


# Set up the constrainsL
HEARTS   = chr(9829)    # Character 9829 is '♥'
DIAMONDS = chr(9830)    # Character 9830 is '♦'
SPADES   = chr(9824)    # Character 9824 is '♠'
CLUBS    = chr(9827)    # Character 9824 is '♣'

BACKSIDE = 'backside'


def main():
    print('''Blackjack by, Obed Banda
    
    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are woth 10 points
    Aces are worth 1 tor 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')

    money = 5000
    while True: # Main group loop.
        # Check if the player has run out of money:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing")
            sys.exit()

        # Let the player enter their bet for this round:
        print("Money:", money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet:', bet)
        while True: # Keep looping until player stands or busts.
            displyaHands(playerHanda, dealerHand, False)
            print(())

            # Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S or D:
            move = getMove(playerHand, money - bet)

            # Handle the player actions
            if move == 'D':
                # Player is doubling down, they can increase their bet:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increase to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/double down takes another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted:
                    continue

                if move in ('S', 'D'):
                    # Stand/doubleing down stops the player's turn
                    break

            # Handle the dealer's actions:
            if getHandValue(dealerHand) > 17:
                # The delader hits:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break   # The dealer has busted.
                input("Press Enter to continue")
                print('\n\n')

        # Show the final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whethe the player won, lost, or tied:
        if dealerValue > 21:
            print('Dealer bursts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
