def sum_digits(start, end):
    total = 0
    for num in range(start, end + 1):
        total += sum(int(digit) for digit in str(num))
    return total
