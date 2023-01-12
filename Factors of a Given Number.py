def find_factors(n):
    if n < 1:
        return []
    else:
        factors = []
        for x in range(1, n + 1):
            if n % x == 0:
                factors.append(x)
        return factors

print(find_factors(9))
            