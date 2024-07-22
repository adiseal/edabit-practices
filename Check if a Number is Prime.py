def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Prime numbers 200 - 300 => 223, 227, 229, 233, 239,241, 251, 257, 263, 269, 271, 277, 281, 283, 293

print(is_prime(200)) # False
print(is_prime(201)) # False
print(is_prime(202)) # False
print(is_prime(203)) # False
print(is_prime(204)) # False
print(is_prime(205)) # False
print(is_prime(206)) # False
print(is_prime(207)) # False
print(is_prime(208)) # False
print(is_prime(209)) # False
print(is_prime(210)) # False
print(is_prime(211)) # False
print(is_prime(212)) # False