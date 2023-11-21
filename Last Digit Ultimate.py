def last_dig(a, b, c):
    last_digit_a = abs(a) % 10
    last_digit_b = abs(b) % 10
    last_digit_c = abs(c) % 10

    return (last_digit_a * last_digit_b) % 10 == last_digit_c
