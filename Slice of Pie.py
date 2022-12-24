def equal_slices(total, people, each):
    return people * each <= total


assert equal_slices(11, 5, 2) == True
# 5 people x 2 slices each = 10 slices < 11 slices 

assert equal_slices(11, 5, 3) == False
# 5 people x 3 slices each = 15 slices > 11 slices

assert equal_slices(8, 3, 2) == True

assert equal_slices(8, 3, 3) == False

assert equal_slices(24, 12, 2) == True