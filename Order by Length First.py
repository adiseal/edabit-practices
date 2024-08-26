def make_grlex(words):
    return sorted(words, key=lambda x: (len(x), x))