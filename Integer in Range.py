def int_within_bounds(n, lower, upper):
    i = range(lower, upper)
    if n == upper or isinstance(n, int) == False or upper == lower or n not in range(lower, upper):
        return False
    else:
        return True


assert int_within_bounds(3, 1, 9) == True

assert int_within_bounds(6, 1, 6) == False

assert int_within_bounds(4.5, 3, 8) == False

assert int_within_bounds(3, 1, 9) == True

assert int_within_bounds(6, 1, 6) == False

assert int_within_bounds(4.5, 3, 8) == False

assert int_within_bounds(-5, -10, 6) == True

assert int_within_bounds(4, 0, 0) == False

assert int_within_bounds(10, 9, 11) == True

assert int_within_bounds(6.3, 2, 6) == False

assert int_within_bounds(6.3, 2, 10) == False

assert int_within_bounds(9, 2, 3) == False

assert int_within_bounds(9, 9, 9) == False
"""
assert int_within_bounds(-3, -5, -2) == True
Test.assert_equals(int_within_bounds(-3, -5, -3), False)
Test.assert_equals(int_within_bounds(-3, -10, 10), True)
Test.assert_equals(int_within_bounds(0, -3, 3), True)
Test.assert_equals(int_within_bounds(0, 0, 1), True)
Test.assert_equals(int_within_bounds(7, 7, 12), True)
"""