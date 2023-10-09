import math

def sine(x, y):
    result = x * math.sin(math.radians(y))
    return round(result, 2)

def cosine(x, y):
    result = x * math.cos(math.radians(y))
    return round(result, 2)

def tangent(x, y):
    result = x * math.tan(math.radians(y))
    return round(result, 2)
