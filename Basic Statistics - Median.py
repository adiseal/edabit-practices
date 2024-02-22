def median(lst):
    n = len(lst)
    s = lst[n // 2]
    if n % 2 == 0:
        return round((s + lst[n // 2 - 1]) / 2, 1)
    else:
        return s