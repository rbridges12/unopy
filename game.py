import uno

class game:
    def __init__(self, players):
        self.players = players
        self.deck = []

    def init_game(self):
        # Create all the cards in the deck
        colors = ["Red", "Blue", "Green", "Yellow"]
        for color in colors:
            # Add 1 zero card
            self.deck.append(uno.Card(color, 0))
            # Add 2 of each other number
            for n in range(1, 10):
                self.deck.append(uno.card(color, n))
                self.deck.append(uno.card(color, n))
            # Add 2 draw 2, skip, and reverse
            for n in range(2):
                self.deck.append(uno.card(color, "draw two"))
                self.deck.append(uno.card(color, "skip"))
                self.deck.append(uno.card(color, "reverse"))
        # Add 4 wildcards and 4 wild draw 4
        for n in range(4):
            self.deck.append(uno.Card("wild", "wildcard"))
            self.deck.append(uno.Card("wild", "draw four"))