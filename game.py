import uno


class Game:

    # Create game object specifying a list of Player objects and optionally a Deck object
    def __init__(self, players, deck=None):

        self.players = players

        # If no deck is specified, make it an empty Deck object
        if deck is None:
            self.deck = uno.Deck()

        # Create a list for played cards and an index for which player's turn it is
        self.played_cards = []
        self.turn = 0

    # Add all necessary cards to the empty Deck
    def init_deck(self):

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

    # Make each player draw their initial hand of 7 cards
    def draw_hands(self):
        for player in self.players:
            for i in range(7):
                player.add_to_hand(self.deck.draw_card())

    # Boolean function to test if any of the players have won
    def player_has_won(self):
        for player in self.players:
            if player.has_won():
                return True
        return False

    # Boolean function to test if the specified card can be played
    def can_play_card(self, card):

        # If no cards have been played, return True
        # TODO: look for a way to handle this case without checking every time
        if self.played_cards == []:
            return True

        # Get the last card played from the end of the list of played cards
        last_card_played = self.played_cards[len(self.played_cards) - 1]
        last_color = last_card_played.get_color()

        # If last played card was wild, get its temporary color
        if last_color == 'wild':
            last_color = last_card_played.get_temp_color()

        # If the specified card and the last card played have the same number or the same color, return true
        if card.get_color() == last_color or card.get_number() == last_card_played.get_number():
            return True

        elif card.get_color() == 'wild':
            return True
        return False

    # Boolean function to test if the specified player has to draw a card, i.e. none of their cards can be played
    def has_to_draw(self, player):
        hand = player.get_hand()
        for card in hand:
            if self.can_play_card(card):
                return False
        return True

    # Make the specified player play a card
    def play_card(self, player):

        self.draw_card_horizontal(player.get_hand())
        # Print out the player's hand
        #i = 1
        #for card in player.get_hand():
         #   print('\nCard %s:' % i)
          #  print(card)
           # i += 1

        # Make the player draw cards until one of them can be played
        # TODO: add functionality for different rule where player only has to draw once
        # TODO: display number of card drawn so it can be picked
        while self.has_to_draw(player):
            name = player.get_name()
            print('%s has to draw' % name)
            draw_card = self.deck.draw_card()
            print('%s drew this card: \n%s' % (name, draw_card))
            player.add_to_hand(draw_card)

        # Ask the player which card to play until the input a valid index
        choice_index = int(input("Which card will you play?\n")) - 1
        print(choice_index)
        while choice_index > 7 or choice_index < 0:
            print("Not a valid choice.")
            choice_index = int(input("Which card will you play?\n")) - 1
        chosen_card = player.get_hand()[choice_index]

        # Ask the player which card to play until the card the choose can be played
        while not self.can_play_card(chosen_card):
            print('Not a valid card choice')
            chosen_card = player.get_hand()[int(input('Which card will you play?\n')) - 1]

        # Add the chosen card to the played cards list
        self.played_cards.append(chosen_card)

        # Remove the played card from the player's hand
        player.remove_from_hand(choice_index)

        # If the played card was wild, have the player choose a new color for the next player
        # TODO: implement this
        # TODO: make all quotes single
        if chosen_card.get_color() == 'wild':
            new_color = input('Choose a new color:\n')
            print('Color changed to %s' % new_color)
            new_color.lower()
            chosen_card.set_temp_color(new_color)

    # Increment the turn index and return it to zero if necessary
    def next_turn(self):

        self.turn += 1
        if self.turn >= len(self.players):
            self.turn = 0

    # Make the given player take their turn
    def do_turn(self, player):

        name = player.get_name()
        # Print which player's turn it is and which turn it is

        print('\n\n\n\n\n\nTurn %s, %s\'s turn: ' % (self.turn, name))

        # If no cards have been played, the player can play a card
        # TODO: find a way to handle this without checking every time
        if self.played_cards == []:
            self.play_card(player)
        else:

            # Get the last played card from the end of the played cards list
            last_card_played = self.played_cards[len(self.played_cards) - 1]

            # Print the previously played card
            print('Previous card:')
            print(last_card_played)
            print('\n\n')

            # Get the "number" of the last card
            last_number = last_card_played.get_number()

            # If the last card was a number, the player can play a card
            if isinstance(last_number, int) or last_number == 'wildcard':

                # Print('last card was a number')
                self.play_card(player)

            # If the last card was a skip, skip the next player
            elif last_number == 'skip':

                # print('last card was a skip')
                self.skip_player(self.players[self.turn % len(self.players)])
                print('%s was skipped' % name)

            # If the last card was a reverse, reverse the turn order
            elif last_number == 'reverse':

                # print('last card was a reverse')
                self.reverse(player)
                print('order reversed')

            # If the last card was a draw 2, make the next player draw 2
            # TODO: fix bug where if a draw 2 is played, loops infinitely bc it keeps making people draw
            elif last_number == 'draw 2':

                # print('last card was a draw 2')
                self.draw_multiple(player, 2)
                print('%s had to draw 2 cards' % name)

            # If the last card was a draw 4, make the next player draw 4
            elif last_number == 'draw 4':

                # print('last card was a draw 4')
                self.draw_multiple(player, 4)
                print('%s had to draw 4 cards' % name)

            # else:
            # print('card is wrong')

    # Initialize the game by creating the deck, shuffling it, and having players draw their hands
    def init_game(self):

        self.init_deck()
        self.deck.shuffle()
        self.draw_hands()

    # Play the game
    def play_game(self):
        current_player = None
        # Do turns until a player has won
        while not self.player_has_won():
            # Get the player who's turn it is
            current_player = self.players[self.turn % len(self.players)]

            # Do their turn and move to the next turn
            self.do_turn(current_player)
            self.turn += 1

        # Print the winning player's name
        print('%s won!' % (current_player.get_name()))

    # get the list of players
    def get_players(self):
        return self.players

    # get the Deck object
    def get_deck(self):
        return self.deck

    # Skip the specified player's turn
    def skip_player(self, player):

        player_index = self.players.index(player)
        self.turn = 1 + player_index

    # Reverse the turn order
    def reverse(self, current_player):

        self.players.reverse()

        # Make sure the turn index remains on the same player
        current_player_index = self.players.index(current_player)
        self.turn = current_player_index

    # Make the specified player draw the specified number of cards
    def draw_multiple(self, player, n):
        for i in range(n):
            player.add_to_hand(self.deck.draw_card())

    # Print out cards horizontally
    def draw_card_horizontal(self, card_list):

        output = ''
        card_lines = []
        for card in card_list:
            card_lines += str(card).split('\n')

        for row in card_lines[0]:
            for lines in card_lines:
                output += lines[row]
        return output


