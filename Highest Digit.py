def highest_digit(num):
    return int(max(list(str(num))))
    


assert highest_digit(379) == 9

assert highest_digit(2) == 2

assert highest_digit(377401) == 7

