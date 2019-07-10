import uno
import game

def make_players(player_names):
  players = []
  for name in player_names:
    players.append(uno.Player(name))
  return players

player_names = ['Riley', 'Raymond']

g = game.Game(make_players(player_names))
g.init_game()
g.play_game()
