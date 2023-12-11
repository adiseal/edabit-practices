import math

def no_perms_digits(n):
    n_factorial = math.factorial(n)
    return len(str(n_factorial))
