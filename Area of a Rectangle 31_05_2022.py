# Author    : Adi Nugroho
# Date      : May/31/2022
# a function that calculates the area of a rectangle
# formula => area of a rectangle = height * width

def area(h, w):
    if h > 0 and w > 0:
        return h * w
    return -1

# print(area(-2, -5)) => -1