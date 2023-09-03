def first_non_repeated_character(s):
    for c in s:
        if s.count(c) == 1:
            return c
    return False
