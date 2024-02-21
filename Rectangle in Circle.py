import math

def rectangle_in_circle(width, height, radius):
    diagonal = math.sqrt(width ** 2 + height ** 2)
    return diagonal <= 2 * radius
