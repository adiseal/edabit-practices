from math import sqrt, pow 

def next_square(n):
    if n % n ** 0.5 == 0:
        return pow((sqrt(n)+1),2)
    else:
        return None