def last(lst, n):
    if n > len(lst):
        return "invalid"
    elif n == 0:
        return []
    else:
        return lst[-n:]
