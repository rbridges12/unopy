import uno.py

class game:
    deck = []
    colors = ["Red","Blue","Green","Yellow"]
    for color in colors:
        for n in range(10):
            deck.add(uno.card(color,n))
