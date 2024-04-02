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

print(is_prime(1)) # False
print(is_prime(2)) # True
print(is_prime(3)) # True
print(is_prime(4)) # False
print(is_prime(5)) # True 
print(is_prime(6)) # False
print(is_prime(7)) # True
print(is_prime(8)) # False
print(is_prime(9)) # False
print(is_prime(10)) # False
print(is_prime(11)) # True
print(is_prime(12)) # False
print(is_prime(13)) # True
print(is_prime(14)) # False
print(is_prime(15)) # False
print(is_prime(16)) # False
print(is_prime(17)) # True
print(is_prime(18)) # False
print(is_prime(19)) # True
print(is_prime(20)) # False
