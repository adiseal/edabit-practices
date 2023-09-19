import math

def area_of_hexagon(x):
    if isinstance(x, int) and x > 0:
        area = (3 * math.sqrt(3) * x**2) / 2
        return round(area, 1)
    else:
        return None
