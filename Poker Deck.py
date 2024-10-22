import random

def gen_deck():
  """Generates a standard 52-card poker deck.

  Returns:
    A list of tuples, where each tuple represents a card. The tuple contains
    the rank (2-14) and the suit (d, c, h, or s) of the card.
  """

  deck = []
  ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
  suits = ["d", "c", "h", "s"]

  for rank in ranks:
    for suit in suits:
      deck.append((rank, suit))

  # Optional: Shuffle the deck
  random.shuffle(deck)

  return deck