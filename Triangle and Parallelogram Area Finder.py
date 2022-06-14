# Author    : Adi Nugroho
# Date      : Jun/14/2022
# a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") 
# as input and calculates the area of that shape

def area_shape(base, height, shape):
    if (type(base) == int and base > 0) and (type(height) == int and height > 0):
        if shape == "triangle":
            return int(eval(str(0.5 * base * height)))
        else:
            return int(eval(str(base * height)))
    else:
        if shape == "triangle":
            return float(eval(str(0.5 * base * height)))
        else:
            return float(eval(str(base * height)))

# print(area_shape(2, 3, "triangle")) ➞ 3
# print(area_shape(8, 6, "parallelogram")) ➞ 48
# print(area_shape(2.9, 1.3, "parallelogram")) ➞ 3.77