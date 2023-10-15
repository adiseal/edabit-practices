def letter_at_position(n):
    if isinstance(n, int) or (isinstance(n, float) and n.is_integer()):
        n = int(n)
        if 1 <= n <= 26:
            return chr(96 + n)
    return "invalid"
