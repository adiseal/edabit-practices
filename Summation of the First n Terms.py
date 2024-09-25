def summation(exp, upper_limit):
    total_sum = 0
    for n in range(1, upper_limit + 1):
        # Evaluate the expression for the current term n
        total_sum += eval(exp)
    # Round the result to the nearest tenth
    return round(total_sum, 1)