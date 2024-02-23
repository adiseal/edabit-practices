def abbreviate(sentence, n=4):
    words = sentence.split()
    abbreviation = [word[0].upper() for word in words if len(word) >= n]
    return ''.join(abbreviation)
