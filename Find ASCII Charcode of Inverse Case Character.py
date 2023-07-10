def counterpartCharCode(char):
    if char.islower():
        return ord(char.upper())
    else:
        return ord(char.lower())
