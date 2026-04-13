"""
Poker Draw Program - Christopher Alvarez

This program uses a Deck class to deal a 5-card poker hand.
The user can choose which cards to replace, and new cards
are drawn from the deck.
"""

import random


# This class represents a deck of cards
class Deck:

    # Sets up the deck with a given size and shuffles it
    def __init__(self, size):
        self.card_list = []

        # Add numbers from 0 up to the deck size
        for i in range(size):
            self.card_list.append(i)

        self.current_card = 0
        self.size = size

        # Shuffle the deck so cards are in random order
        random.shuffle(self.card_list)

    # Deals one card from the deck
    def deal(self):
        # If all cards have been used, shuffle and start over
        if self.current_card >= self.size:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling deck...")

        # Take the next card from the deck
        card = self.card_list[self.current_card]
        self.current_card += 1
        return card


# Converts a number into a readable card (rank and suit)
def card_to_string(card):
    ranks = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    # Use math to figure out rank and suit
    rank = ranks[card % 13]
    suit = suits[card // 13]

    return f"{rank} of {suit}"


# Deals a hand of 5 cards from the deck
def deal_hand(deck):
    hand = []
    for i in range(5):
        hand.append(deck.deal())
    return hand


# Displays the current hand with position numbers
def print_hand(hand):
    print("\nYour hand:")
    for i in range(len(hand)):
        print(f"{i + 1}: {card_to_string(hand[i])}")


# Allows the user to choose which cards to replace
def draw_phase(deck, hand):
    print("\nEnter positions of cards to replace")
    user_input = input("Cards to replace: ")

    # If nothing is entered, keep the same hand
    if user_input.strip() == "":
        return hand

    # Replace commas with spaces so both formats work
    user_input = user_input.replace(',', ' ')
    positions = user_input.split()

    for pos in positions:
        index = int(pos) - 1

        # Replace selected card
        if index >= 0 and index < 5:
            hand[index] = deck.deal()

    return hand


# Main function to run the program
def main():
    print("=== Poker Draw Game ===")

    deck = Deck(52)

    # Deal the initial 5-card hand
    hand = deal_hand(deck)
    print_hand(hand)

    # Let the user replace selected cards
    hand = draw_phase(deck, hand)

    # Display the final hand after drawing
    print("\n=== Final Hand ===")
    print_hand(hand)


# Run the program
main()
