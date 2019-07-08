# Virtual UNO Classes

class Player:
    # Initialize player with specified name and han of cards, empty by default
    def __init__(self, name, hand=None):
        self.name = name
        if hand == None:
            self.hand = []

    def add_to_hand(self, card):
        self.hand.append(card)

    def set_hand(self, hand):
        self.hand = hand

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Card:
    def __init__(self, color, number):
        # TODO: error catching for invalid colors/numbers?
        self.color = color
        self.number = number

    def  get_color(self):
        return self.color

    def get_number(self):
        return self.number

