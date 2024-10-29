def little_big(n):
    if n % 2 == 1:  # Odd position
        return 5 + (n // 2)
    else:  # Even position
        return 100 * (2 ** ((n // 2) - 1))