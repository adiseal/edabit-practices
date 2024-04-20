from collections import Counter

def is_full_house(hand):
    counts = Counter(hand)
    return 2 in counts.values() and 3 in counts.values()