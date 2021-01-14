import uno
import game
#import tests
import random

logger = uno.GameLogger()
# Turn list of player names into Player objects
def make_players(player_names_list):
    players = []
    for name in player_names_list:
        players.append(uno.Player(name))
    return players

# Randomize the order of the player names and therefore the turn order
def randomize_order(player_names_list):
  for i in len(player_names_list):
    random_index = random.randint(1, len(player_names_list) -1)
    temp_name = player_names_list.pop(random_index)
    player_names_list.append(temp_name)

print("Welcome to Unopy!")
# List of player names
player_names = [];
exit_name_input = False;
while not exit_name_input:
    player_name = input("\n\nEnter a player name or hit enter if all names have been entered:\n")
    if player_name == '':
        exit_name_input = True
    else:
        player_names.append(player_name);

# Create a new game with the list of players
g = game.Game(make_players(player_names))
# Initialize the game
g.init_game()
#c1 = uno.Card('yellow', 5)
#c1.setColor('red')
#print(c1.get_x())
#print(c1.scale(4,6))

# Play the game
g.play_game()