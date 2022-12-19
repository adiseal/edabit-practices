def nothing_is_nothing(*args):
    x = all(args)
    return x
    

assert nothing_is_nothing(0, False, [], {}) == False
assert nothing_is_nothing(33, "Hello", (True, True, 3)) == True
assert nothing_is_nothing(True, None) == False