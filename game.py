import uno


class Game:

    # Create game object specifying a list of Player objects, an optional Deck object, and an optional GameLogger object
    def __init__(self, players, deck=None, logger=None):

        self.players = players

        # If no deck is specified, make it an empty Deck object
        if deck is None:
            self.deck = uno.Deck()

        # If logger is not specified, make a new one
        if logger is None:
          self.logger = uno.GameLogger()
          
        # Create an index for which player's turn it is
        self.turn = 0
        self.player_index = 0

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

        # Get the last card played from the end of the list of played cards
        last_card_played = self.deck.discard_pile[-1]
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

        name = player.get_name()
        new_color = ''

        # Make the player draw cards until one of them can be played
        # TODO: add functionality for different rule where player only has to draw once
        # TODO: display number of card drawn so it can be picked
        while self.has_to_draw(player):
            draw_input = input("\nYou do not have a playable card at hand,  enter 'draw' to draw another card:\n")
            draw_input = draw_input.lower();
            if draw_input == 'draw':
                draw_card = self.deck.draw_card()
                print('\n%s drew this card: \n%s' % (name, draw_card))
                player.add_to_hand(draw_card)
                last_card_played = self.deck.discard_pile[-1]
                if last_card_played.get_color() == 'wild':
                    print('\nThe current color is %s.\n' % last_card_played.get_temp_color())
                else:
                    print('\nThe current color is %s.\n' % last_card_played.get_color())
            else:
                print("\nDraw failed. Try again:")

        print("Your current hand:\n")
        self.print_hand(player)
        
        # Ask the player which card to play until they input a valid index
        choice_index = player.choose_card()
        chosen_card = player.get_hand()[choice_index]

        # Ask the player which card to play until the card they choose can be played
        while not self.can_play_card(chosen_card):
            print('\nYou cannot play that card.')
            chosen_card = player.get_hand()[player.choose_card()]

        # Add the chosen card to the played cards list
        self.deck.discard_pile.append(chosen_card)

        # Remove the played card from the player's hand
        player.remove_from_hand(choice_index)

        # If the played card was wild, have the player choose a new color for the next player
        # TODO: implement this
        # TODO: make all quotes single
        if chosen_card.get_color() == 'wild':
            new_color = player.choose_color()
            new_color = new_color.lower()

            while (new_color != 'red' and new_color != 'yellow' and new_color != 'blue' and new_color != 'green'):
                new_color = input("\nInvalid color. Try again:\n")
                new_color = new_color.lower()

            chosen_card.set_temp_color(new_color)
        
        elif chosen_card.get_number() == 'skip':
          next_player = self.players[(self.player_index + 1) % len(self.players)]
          self.skip_next_player()
          print('%s was skipped.' % next_player.get_name())

        elif chosen_card.get_number() == 'draw 2':
          next_player = self.players[(self.player_index + 1) % len(self.players)]
          self.draw_multiple(next_player, 2)
          self.skip_next_player()
          print('\n%s had to draw 2 cards.' % next_player.get_name())
        
        elif chosen_card.get_number() == 'reverse':
          self.reverse(player)
          print('\n\nThe order was reversed.')

        if chosen_card.get_number() == 'draw 4':
          next_player = self.players[(self.player_index + 1) % len(self.players)]
          self.draw_multiple(next_player, 4)
          self.skip_next_player()
          print('\n\n%s had to draw 4 cards.' % next_player.get_name())

    # Make the given player take their turn
    def do_turn(self, player):
        name = player.get_name()

        # Print which player's turn it is and which turn it is
        print('\n\n\nTurn %d, %s\'s turn:' % (self.turn+1, name))

        # Get the last played card from the end of the played cards list
        last_card_played = self.deck.discard_pile[-1]

        if last_card_played.get_color() == 'wild':
            print('\nThe color has been changed to %s.' % last_card_played.get_temp_color())

        # Print the previously played card
        print('\nPrevious card:')
        print(last_card_played)
        print('\n\n')

        # Get the "number" of the last card
        # last_number = last_card_played.get_number()

          # Print('last card was a number')
        self.play_card(player)

    # Initialize the game by creating the deck, shuffling it, and having players draw their hands
    def init_game(self):

        self.deck.init_deck()
        self.deck.shuffle()
        self.draw_hands()
        starter_flag = False;
        self.deck.discard_pile = [];

        while not starter_flag:
            self.deck.discard_pile.append(self.deck.draw_card())
            last_card_num = self.deck.discard_pile[-1].get_number()
            if last_card_num != 'draw 4' and last_card_num != 'wildcard':
                starter_flag = True;
            else:
                print(self.deck.discard_pile[-1])
                print("\nDrawing another card...The first card flipped was invalid.")
                        
    # Play the game
    def play_game(self):
        current_player = None
        # Do turns until a player has won
        while not self.player_has_won():
            # Get the player who's turn it is
            current_player = self.players[self.player_index] 
            #self.turn % len(self.players)

            # Do their turn and move to the next turn
            self.do_turn(current_player)
            self.player_index += 1
            self.player_index %= len(self.players)
            self.turn += 1

        # Print the winning player's name
        print('\n%s won!' % (current_player.get_name()))

    # get the list of players
    def get_players(self):
        return self.players

    # get the Deck object
    def get_deck(self):
        return self.deck

    # Skip the specified player's turn
    def skip_next_player(self):
        self.player_index += 1

    # Reverse the turn order
    def reverse(self, current_player):

        self.players.reverse()

        # Make sure the turn index remains on the same player
        current_player_index = self.players.index(current_player)
        self.player_index = current_player_index

    # Make the specified player draw the specified number of cards
    def draw_multiple(self, player, n):
        for i in range(n):
            player.add_to_hand(self.deck.draw_card())

    # Print out cards horizontally
    def draw_card_horizontal(self, card_list):

        # create empty str for output and empty list for storing lists of card lines
        output = ''
        card_lines = []
        for card in card_list:

          # Split each card into its individual lines
          split_card = str(card).split('\n')

          # Color each line separately because split method messes up color
          for i in range(len(split_card)):
            split_card[i] = uno.get_color_str(card.get_color()) + split_card[i] + uno.bcolors.ENDC

          # Add list of colored lines to the master list
          card_lines.append(split_card)

        # for every row, get that row of each card and put them together, then put a newline at the end
        for row_index in range(len(card_lines[0])):
            for lines in card_lines:
                output += lines[row_index]
                output += ' '
            output += '\n'
        return output

    # Print out the player's hand
    def print_hand(self, player):
        hand = player.get_hand()
        card_nums = ''

        # print normally if less than 6 cards
        if len(hand) <= 6:
          for i in range(len(hand)):
            card_nums += ' ' + str(i+1)
            card_nums += ' ' * (len(str(hand[0]).split('\n')[1])-1)
          print('\n' + card_nums)
          print(self.draw_card_horizontal(hand))
        
        # split into 6 card rows to prevent console overlap
        else:
          card_index = 0;
          for i in range((len(hand) // 6) + 1):
            temp_hand = hand[card_index:card_index + 6]
            card_nums = ''
            for j in range(len(temp_hand)):
              card_nums += ' %d' %(card_index+j+1)
              card_nums += ' ' * (len(str(temp_hand[0]).split('\n')[1])-1)
            card_index += len(temp_hand)
            print(card_nums)
            print(self.draw_card_horizontal(temp_hand))
            