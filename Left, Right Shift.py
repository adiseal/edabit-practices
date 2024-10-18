def left_shift(lst, n):
    # Use modulo to ensure n is within the list's length
    n = n % len(lst)
    return lst[n:] + lst[:n]

def right_shift(lst, n):
    # Use modulo to ensure n is within the list's length
    n = n % len(lst)
    return lst[-n:] + lst[:-n]