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

# Prime numbers 200 - 300 => 229, 233, 239,241, 251, 257, 263, 269, 271, 277, 281, 283, 293

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
print(is_prime(213)) # False
print(is_prime(214)) # False
print(is_prime(215)) # False
print(is_prime(216)) # False
print(is_prime(217)) # False
print(is_prime(218)) # False
print(is_prime(219)) # False
print(is_prime(220)) # False
print(is_prime(221)) # False
print(is_prime(222)) # False
print(is_prime(223)) # True
print(is_prime(224)) # False
print(is_prime(225)) # False
print(is_prime(226)) # False
print(is_prime(227)) # False
print(is_prime(228)) # False
print(is_prime(229)) # False