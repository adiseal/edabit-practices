def get_triangle_type(lst):
    if len(lst) == 3:
        a = set(lst)
        if len(a) == 1:
            return "equilateral"
        elif len(a) == 2:
            return "isosceles"
        elif len(a) == 3:
            return "scalene"
    else:
        return "not a triangle"
        
print(get_triangle_type([8, 8, 8])) # "equilateral"