# Virtual UNO Classes

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

    # Set the player's hand to a specific list of cards
    def set_hand(self, hand):
        self.hand = hand

    # Set the player's name
    def set_name(self, name):
        self.name = name

    # Get the player's name
    def get_name(self):
        return self.name


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

