def shift_to_right(x, y):
    # Base case: when y reaches 0, return the original number x
    if y == 0:
        return x
    # Recursive case: divide x by 2 and reduce y by 1
    return shift_to_right(x // 2, y - 1)