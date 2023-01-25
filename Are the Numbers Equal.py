def is_equal(num1, num2):
    if num1 != num2 or type(num1) == str:
        return False
    else:
        return True


assert is_equal(5, 6) == False

assert is_equal(1, 1) == True

assert is_equal("1", 1) == False

assert is_equal("1", 1) == False
