from math import sqrt

def perfect_roots(n):
    isit = sqrt(n)
    return isit.is_integer()


print(perfect_roots(1000)) #➞ False