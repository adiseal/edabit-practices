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

# Prime numbers 100 - 200 => 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199


print(is_prime(100)) # False
print(is_prime(101)) # True
print(is_prime(102)) # False
print(is_prime(103)) # True
print(is_prime(104)) # False
print(is_prime(105)) # False
print(is_prime(106)) # False
print(is_prime(107)) # True