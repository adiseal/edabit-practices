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

# Prime numbers 100 - 200 => 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199


print(is_prime(100)) # False
print(is_prime(101)) # True
print(is_prime(102)) # False
print(is_prime(103)) # True
print(is_prime(104)) # False
print(is_prime(105)) # False
print(is_prime(106)) # False
print(is_prime(107)) # True
print(is_prime(108)) # False
print(is_prime(109)) # True
print(is_prime(110)) # False
print(is_prime(111)) # False
print(is_prime(112)) # False
print(is_prime(113)) # True
print(is_prime(114)) # False
print(is_prime(115)) # False
print(is_prime(116)) # False
print(is_prime(117)) # False
print(is_prime(118)) # False
