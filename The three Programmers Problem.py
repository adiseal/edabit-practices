def programmers(one, two, three):
    max_valued = max(one, two, three)
    min_valued = min(one, two, three)
    diff_paid = max_valued - min_valued
    return diff_paid 

assert programmers(147, 33, 526) == 493
assert programmers(33, 72, 74) == 41
assert programmers(1, 5, 9) == 8
    