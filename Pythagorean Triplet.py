def is_triplet(a, b, c):
    lst = [a, b, c]
    lst.sort()
    return lst[0]**2 + lst[1]**2 == lst[2]**2
