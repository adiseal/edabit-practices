import math

def cone_volume(h, r):
    volume = (1/3) * math.pi * r**2 * h
    return round(volume, 2)
