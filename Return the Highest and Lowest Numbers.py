def high_low(txt):
    numbers = [int(x) for x in txt.split()]
    return "{} {}".format(max(numbers), min(numbers))
