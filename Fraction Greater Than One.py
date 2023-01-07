def greater_than_one(frac):
    quantifier, divider = frac.split("/")
    return (float(quantifier) / float(divider)) > 1
    


assert greater_than_one("1/2") == False

assert greater_than_one("7/4") == True

assert greater_than_one("10/10") == False
            