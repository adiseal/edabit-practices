def legendre(p, n):
    exponent = 0
    power = p
    while power <= n:
        exponent += n // power
        power *= p
    return exponent