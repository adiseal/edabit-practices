def millions_rounding(lst):
    millions = []
    for x in lst:
        x[1] = int(round(x[1], -6))
        millions = millions+[x]
    return millions
    