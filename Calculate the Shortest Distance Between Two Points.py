import math

def shortestDistance(s):
    coordinates = s.split(',')
    x1, y1, x2, y2 = map(float, coordinates)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)