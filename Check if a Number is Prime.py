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

# Prime numbers => 97

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
print(is_prime(21)) # False
print(is_prime(22)) # False
print(is_prime(23)) # True
print(is_prime(24)) # False
print(is_prime(25)) # False
print(is_prime(26)) # False
print(is_prime(27)) # False
print(is_prime(28)) # False
print(is_prime(29)) # True
print(is_prime(30)) # False
print(is_prime(31)) # True
print(is_prime(32)) # False
print(is_prime(33)) # False
print(is_prime(34)) # False
print(is_prime(35)) # False
print(is_prime(36)) # False
print(is_prime(37)) # True
print(is_prime(38)) # False
print(is_prime(39)) # False
print(is_prime(40)) # False
print(is_prime(41)) # True
print(is_prime(42)) # False
print(is_prime(43)) # True
print(is_prime(44)) # False
print(is_prime(45)) # False
print(is_prime(46)) # False
print(is_prime(47)) # True
print(is_prime(48)) # False
print(is_prime(49)) # False
print(is_prime(50)) # False
print(is_prime(51)) # False
print(is_prime(52)) # False
print(is_prime(53)) # True
print(is_prime(54)) # False
print(is_prime(55)) # False
print(is_prime(56)) # False
print(is_prime(57)) # False
print(is_prime(58)) # False
print(is_prime(59)) # True
print(is_prime(60)) # False
print(is_prime(61)) # True
print(is_prime(62)) # False
print(is_prime(63)) # False
print(is_prime(64)) # False
print(is_prime(65)) # False
print(is_prime(66)) # False
print(is_prime(67)) # True
print(is_prime(68)) # False
print(is_prime(69)) # False
print(is_prime(70)) # False
print(is_prime(71)) # True
print(is_prime(72)) # False
print(is_prime(73)) # True
print(is_prime(74)) # False
print(is_prime(75)) # False
print(is_prime(76)) # False
print(is_prime(77)) # False
print(is_prime(78)) # False
print(is_prime(79)) # True
print(is_prime(80)) # False
print(is_prime(81)) # False
print(is_prime(82)) # False
print(is_prime(83)) # True
print(is_prime(84)) # False
print(is_prime(85)) # False
print(is_prime(86)) # False
print(is_prime(87)) # False
print(is_prime(88)) # False
print(is_prime(89)) # True
print(is_prime(90)) # False
print(is_prime(91)) # False
print(is_prime(92)) # False
print(is_prime(93)) # False
print(is_prime(94)) # False