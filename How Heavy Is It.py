import math

def weight(r, h):
    volume = math.pi * r**2 * h
    volume_in_dm3 = volume / 1000
    mass = volume_in_dm3
    return round(mass, 2)

print(weight(4, 10)) # 0.5