# Virtual UNO Classes

import random
from termcolor import colored


class Player:
    # Initialize player with specified name and hand of cards, empty by default
    def __init__(self, name, hand=None):
        self.name = name
        if hand == None:
            self.hand = []

    # Add a card to the player's hand
    def add_to_hand(self, card):
        self.hand.append(card)

    # Remove a card from the players hand, specifying the index of the card in the list of cards in hand
    def remove_from_hand(self, card_index):
        self.hand.pop(card_index)

    def has_won(self):
        if len(self.hand) == 0:
            return True
        return False

    # Set the player's hand to a specific list of cards
    def set_hand(self, hand):
        self.hand = hand

    # Set the player's name
    def set_name(self, name):
        self.name = name

    # Get the player's name
    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand


class Card:
    # Initialize the card with specified color and number
    def __init__(self, color, number):
        # TODO: error catching for invalid colors/numbers?
        self.color = color
        self.number = number

    # Get the card's color
    def  get_color(self):
        return self.color

    # Get the card's number
    def get_number(self):
        return self.number

    def __str__(self):
        spacing = ''
        for i in range(10 - len(str(self.number))):
            spacing += ' '

        card_str = ' __________ \n|%s%s|\n|          |\n|          |\n|          |\n|          |\n|__________|' % (
        self.number, spacing)

        color_list = ['red', 'green', 'yellow', 'blue']
        if self.color in (color_list):
            return colored(card_str, self.color)
        else:
            return colored(card_str, 'magenta')


class Deck:
    def __init__(self, card_list=None):
        if card_list is None:
            self.card_list = []

    def add_card(self, card):
        self.card_list.append(card)

    def shuffle(self):
        for card in self.card_list:
            random_index = random.randint(0, len(self.card_list) - 1)
            temp_card = self.card_list.pop(random_index)
            self.card_list.append(temp_card)

    def draw_card(self):
        card = self.card_list.pop(len(self.card_list) - 1)
        return card

    def get_card(self, index):
        return self.card_list[index]

    def get_card_list(self):
        return self.card_list

    def __str__(self):
        output = ''
        for card in self.card_list:
            output += str(card) + '\n'
        return output







