def char_index(word, char):
    if char not in word:
        return None
    else:
        first_index = word.index(char)
        last_index = len(word) - 1 - word[::-1].index(char)
        return [first_index, last_index]

print(char_index("hello", "l")) # [2, 3]
print(char_index("circumlocution", "c")) # [0, 8]
print(char_index("happy", "h")) # [0, 0]
print(char_index("happy", "e")) # None