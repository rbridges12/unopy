# Virtual UNO Classes

from termcolor import colored
import random


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

    # Get the player's hand
    def get_hand(self):
        return self.hand


class Card:
    # Initialize the card with specified color and number
    def __init__(self, color, number):

        # TODO: error catching for invalid colors/numbers?
        self.color = color
        self.number = number
        if self.color == 'wild':
            self.temp_color = None

    # If the card is wild, set it's temporary color to the specified color
    def set_temp_color(self, temp_color):
        self.temp_color = temp_color

    # Get the card's color
    def get_color(self):
        return self.color

    # If the card is wild, get its temporary color to play off of
    def get_temp_color(self):
        return self.temp_color

    # Get the card's number
    def get_number(self):
        return self.number

    # Format card to a string graphic to display in terminal
    def __str__(self):

        # Get proper spacing for line on card with the card type
        spacing = ''
        for i in range(10 - len(str(self.number))):
            spacing += ' '

        # Creating card graphics
        card_str = ' __________ \n|%s%s|\n|          |\n|          |\n|          |\n|          |\n|__________|' % (
            self.number, spacing)
        color_list = ['red', 'green', 'yellow', 'blue']

        # Returns color of card
        if self.color in (color_list):
            return colored(card_str, self.color)
        else:
            return colored(card_str, 'magenta')

    # Allow for card size scaling
    def str_scale(self, width, height=None):
        pass


class Deck:
    def __init__(self, card_list=None):

        # Initializes empty card list if no cards are appended to the deck
        if card_list is None:
            self.card_list = []

    # Adds card to deck
    def add_card(self, card):
        self.card_list.append(card)

    # Shuffles deck
    def shuffle(self):
        for card in self.card_list:
            random_index = random.randint(0, len(self.card_list) - 1)
            temp_card = self.card_list.pop(random_index)
            self.card_list.append(temp_card)

    # Returns a drawn card from deck
    def draw_card(self):
        card = self.card_list.pop(len(self.card_list) - 1)
        return card

    # Returns the index of the card
    def get_card(self, index):
        return self.card_list[index]

    # returns the deck
    def get_card_list(self):
        return self.card_list

    # Returns deck with card visuals
    def __str__(self):
        output = ''
        for card in self.card_list:
            output += str(card) + '\n'
        return output
