def alph_num(s: str) -> str:
    return ' '.join([str(ord(c) - ord('A')) for c in s])

print(alph_num("XYZ")) # "23 24 25"
print(alph_num("ABCDEF")) # "0 1 2 3 4 5"
print(alph_num("JAVASCRIPT")) # "9 0 21 0 18 2 17 8 15 19"