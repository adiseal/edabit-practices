def alph_num(s: str) -> str:
    return ' '.join([str(ord(c) - ord('A')) for c in s])

print(alph_num("XYZ")) # "23 24 25"