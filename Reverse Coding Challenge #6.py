def mystery_func(n):
    result = 1
    for digit in str(n):
        result *= int(digit)
    return result
