def high_low(txt):
    numbers = [int(x) for x in txt.split()]
    return "{} {}".format(max(numbers), min(numbers))
    
print(high_low("1 2 3 4 5")) # "5 1"
print(high_low("1 2 -3 4 5")) # "5 -3"
print(high_low("1 9 3 4 -5")) # "9 -5"
print(high_low("13")) # "13 13"
