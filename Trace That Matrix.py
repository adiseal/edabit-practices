def trace(lst):
    a = 0
    q = 0
    for i in lst:
        q = q + i[a]
        a = a + 1
        continue
    return q