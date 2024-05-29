def simple_numbers(a, b):
    simple_nums = []
    for num in range(a, b+1):
        digits = [int(d) for d in str(num)]
        if sum(digit ** (i+1) for i, digit in enumerate(digits)) == num:
            simple_nums.append(num)
    return simple_nums