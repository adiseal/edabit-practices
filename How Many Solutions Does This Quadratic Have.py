def solutions(a, b, c):
    # calculate the discriminant
    discriminant = b**2 - 4*a*c
    # if discriminant is positive, there are two solutions
    if discriminant > 0:
        return 2
    # if discriminant is zero, there is one solution
    elif discriminant == 0:
        return 1
    # if discriminant is negative, there are no real solutions
    else:
        return 0
