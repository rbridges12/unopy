import uno
import random

class Game:

    def __init__(self, players, deck=None):
        self.players = players
        if deck is None:
            self.deck = uno.Deck()
        self.played_cards = []
        self.turn_index = 0

    def init_deck(self):
        # Create all the cards in the deck
        colors = ["red", "blue", "green", "yellow"]
        for color in colors:
            # Add 1 zero card
            self.deck.add_card(uno.Card(color, 0))
            # Add 2 of each other number
            for n in range(1, 10):
                self.deck.add_card(uno.Card(color, n))
                self.deck.add_card(uno.Card(color, n))
            # Add 2 draw 2, skip, and reverse
            for n in range(2):
                self.deck.add_card(uno.Card(color, "draw two"))
                self.deck.add_card(uno.Card(color, "skip"))
                self.deck.add_card(uno.Card(color, "reverse"))
        # Add 4 wildcards and 4 wild draw 4
        for n in range(4):
            self.deck.add_card(uno.Card("wild", "wildcard"))
            self.deck.add_card(uno.Card("wild", "draw four"))

    def draw_hands(self):
        for player in self.players:
            for i in range(7):
                player.add_to_hand(self.deck.draw_card())

    def player_has_won(self):
        for player in self.players:
            if player.has_won():
                return True
        return False

    def can_play_card(self, card):
        if self.played_cards == []:
            return True
        last_card_played = self.played_cards[len(self.played_cards) - 1]
        if card.get_color() == last_card_played.get_color() or card.get_number() == last_card_played.get_number():
            return True
        if card.get_color() == 'wild':
            return True
        return False

    def play_card(self, player):
        print('%s\'s turn: ' % (player.get_name()))
        i = 1
        for card in player.get_hand():
            print('Card %s:' % (i))
            print(card)
            i += 1
        choice_index = int(input("Which card will you play?\n")) - 1
        chosen_card = player.get_hand()[choice_index]
        if self.can_play_card(chosen_card):
            self.played_cards.append(chosen_card)
            player.remove_from_hand(choice_index)
            if chosen_card.get_color() == 'wild':
                new_color = input("Choose a new color:\n")
        else:
            print("You cannot play that card")

    def next_turn(self):
        self.turn_index += 1
        if self.turn_index >= len(self.players):
            self.turn_index = 0

    def do_turn(self, player):
        if self.played_cards == []:
            self.play_card(player)
        else:
            last_card_played = self.played_cards[len(self.played_cards) - 1]
            last_number = last_card_played.get_number()
            if type(last_number) == 'int':
                self.play_card(player)
            elif last_number == 'skip':
                self.skip_player(player)
                print('%s was skipped' % (player.get_name()))
            elif last_number == 'reverse':
                self.reverse()
                print('order reversed')
            elif last_number == 'draw 2':
                self.draw_multiple(player, 2)
                print('%s had to draw 2 cards' % (player.get_name()))
            elif last_number == 'draw 4':
                self.draw_multiple(player, 4)
                print('%s had to draw 4 cards' % (player.get_name()))

    def init_game(self):
        self.init_deck()
        # print(self.deck)
        self.deck.shuffle()
        # print(self.deck)
        self.draw_hands()

    def play_game(self):
        current_player = None
        while not self.player_has_won():
            print('loop')
            current_player = self.players[self.turn_index]
            self.do_turn(current_player)
            self.next_turn()
        print('%s won!' % (current_player.get_name()))

    def get_players(self):
        return self.players

    def get_deck(self):
        return self.deck

    def skip_player(self, player):
        self.turn_index += 1

    def reverse(self, current_player):
        self.players.reverse()
        current_player_index = self.players.index(current_player)
        self.turn_index = current_player_index

    def draw_multiple(self, player, n):
        for i in range(n):
            player.add_to_hand(self.deck.draw_card())








