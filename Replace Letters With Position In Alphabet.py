def alphabet_index(s):
    return ' '.join(str(ord(c) - 96) for c in s.lower() if c.isalpha())