def logarithm(base, number):
    # Check validity of input
    if base <= 1 or number <= 0:
        return "Invalid"
    if base == 1 and number != 1:
        return "Invalid"
    
    exponent = 0
    power = 1    
    while power < number:
        power *= base
        exponent += 1
        if power == number:
            return exponent    
    return "Invalid"