def check_square_and_cube(lst):
    num1, num2 = lst
    sqrt_num1 = num1 ** 0.5
    cbrt_num2 = num2 ** (1/3)
    return round(sqrt_num1, 8) == round(cbrt_num2, 8)
