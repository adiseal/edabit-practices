def to_scottish_screaming(s):
    vowels = 'aeiou'
    return ''.join(['E' if c.lower() in vowels else c for c in s]).upper()
