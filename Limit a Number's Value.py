def limit_number(num, range_low, range_high):
    if num > range_low and num < range_high:
        return num
    elif num <= range_low:
        return range_low
    elif num >= range_high:
        return range_high

"""        
assert limit_number(5, 1, 10) == 5

assert limit_number(-3, 1, 10) == 1

assert limit_number(14, 1, 10) == 10

assert limit_number(4.6, 1, 10) == 4.6 
"""
print(limit_number(-100, -73, -70)) # -> -73 