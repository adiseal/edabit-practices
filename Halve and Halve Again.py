def halve_count(a, b):
    c = []
    while a > b:
        a = a / 2
        if a < b:
            return len(c)
        c = c + [a]