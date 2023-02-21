def check_factors(factors, num):
    return all(num % x == 0 for x in factors)


print(check_factors([1, 2, 50], 100))