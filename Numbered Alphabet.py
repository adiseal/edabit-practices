def alph_num(s: str) -> str:
    return ' '.join([str(ord(c) - ord('A')) for c in s])
