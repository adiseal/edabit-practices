def power_of_two(n):
    while n % 2 == 0 and n > 1:
        n //= 2
    return n == 1