# Virtual UNO Classes
import random


class bcolors:
    YELLOW = '\033[38;5;226m'
    BLUE = '\033[38;5;27m'
    RED = '\033[38;5;196m'
    GREEN = '\033[38;5;76m'
    WILD = '\033[38;5;93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_color_str(color):
    color_str = ''
    if color == 'yellow':
        color_str = bcolors.YELLOW

    elif color == 'blue':
        color_str = bcolors.BLUE

    elif color == 'red':
        color_str = bcolors.RED

    elif color == 'green':
        color_str = bcolors.GREEN

    elif color == 'wild':
        color_str = bcolors.WILD

    return color_str


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

    # Res whether the player has won
    def has_won(self):
        # If their hand is empty, return true
        if len(self.hand) == 0:
            return True
        return False

    # Ask the player which card to choose and return the chosen index
    def choose_card(self):

        choice_index = int(input("\nWhich card will you play?\n")) - 1
        while choice_index > len(self.hand) - 1 or choice_index < 0:
            print("\nNot a valid choice.")
            choice_index = int(input("\nWhich card will you play?\n")) - 1
        return choice_index

    # Ask the player which color to set
    # TODO: check for a valid color here
    def choose_color(self):
        return input('\nChoose the next color:\n')

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

    # Sets color
    def set_color(self, color):
        self.color = color

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

        # Color the card
        return get_color_str(self.color) + card_str + bcolors.ENDC


# TODO: add functionality for when deck is empty
class Deck:
    def __init__(self, card_list=None):

        # Initializes empty card list if no cards are appended to the deck
        if card_list is None:
            self.card_list = []

        self.discard_pile = []

    # Adds card to deck
    def add_card(self, card):
        self.card_list.append(card)

    # Add all necessary cards to the empty Deck
    def init_deck(self):

        colors = ["red", "blue", "green", "yellow"]
        for color in colors:

            # Add 1 zero card
            self.add_card(Card(color, 0))

            # Add 2 of each other number
            for n in range(1, 10):
                self.add_card(Card(color, n))
                self.add_card(Card(color, n))

            # Add 2 draw 2, skip, and reverse
            for n in range(2):
                self.add_card(Card(color, "draw 2"))
                self.add_card(Card(color, "skip"))
                self.add_card(Card(color, "reverse"))

                # Add 4 wildcards and 4 wild draw 4
            for n in range(2):
                self.add_card(Card("wild", "wildcard"))
                self.add_card(Card("wild", "draw 4"))

    # Shuffles deck
    def shuffle(self):
        for card in self.card_list:
            random_index = random.randint(0, len(self.card_list) - 1)
            temp_card = self.card_list.pop(random_index)
            self.card_list.append(temp_card)

    def reshuffle(self):
        print("\nDeck is empty. Reshuffling...")
        if len(self.discard_pile) <= 1:
            raise RuntimeError

        self.card_list = self.discard_pile[:-1]
        self.discard_pile = self.discard_pile[-1:]
        self.shuffle()

    # Returns a drawn card from deck
    def draw_card(self):
        if not self.card_list:
            try:
                self.reshuffle()
            except RuntimeError:
                print("\nThe deck is completely empty...Ending the game.")
                exit(1)

        card = self.card_list.pop()
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


class UnoBot(Player):
    def __init__(self, name, hand=None):
        super().__init__(name, hand)

    def choose_card(self):
        pass

    def choose_color(self):
        pass
