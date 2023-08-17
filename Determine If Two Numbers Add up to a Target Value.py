def sum_of_two(a, b, target):
    for num1 in a:
        for num2 in b:
            if num1 + num2 == target:
                return True
    return False
