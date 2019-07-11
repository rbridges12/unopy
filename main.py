import uno
import game

def make_players(player_names):
  players = []
  for name in player_names:
    players.append(uno.Player(name))
  return players

player_names = ['Riley', 'Raymond', 'Chris']
print(type(1))
g = game.Game(make_players(player_names))
g.init_game()
g.play_game()
