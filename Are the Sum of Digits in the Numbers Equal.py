def is_equal(lst):
    return sum(int(digit) for digit in str(lst[0])) == sum(int(digit) for digit in str(lst[1]))