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

# Prime numbers 100 - 200 => 191, 193, 197, 199


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
print(is_prime(119)) # False
print(is_prime(120)) # False
print(is_prime(121)) # False
print(is_prime(122)) # False
print(is_prime(123)) # False
print(is_prime(124)) # False
print(is_prime(125)) # False
print(is_prime(126)) # False
print(is_prime(127)) # True
print(is_prime(128)) # False
print(is_prime(129)) # False
print(is_prime(130)) # False
print(is_prime(131)) # True
print(is_prime(132)) # False
print(is_prime(133)) # False
print(is_prime(134)) # False
print(is_prime(135)) # False
print(is_prime(136)) # False
print(is_prime(137)) # True
print(is_prime(138)) # False
print(is_prime(139)) # True
print(is_prime(140)) # False
print(is_prime(141)) # False
print(is_prime(142)) # False
print(is_prime(144)) # False
print(is_prime(145)) # False
print(is_prime(146)) # False
print(is_prime(147)) # False
print(is_prime(148)) # False
print(is_prime(149)) # True
print(is_prime(150)) # False
print(is_prime(151)) # False
print(is_prime(152)) # False
print(is_prime(153)) # False
print(is_prime(154)) # False
print(is_prime(155)) # False
print(is_prime(156)) # False
print(is_prime(157)) # True
print(is_prime(158)) # False
print(is_prime(159)) # False
print(is_prime(160)) # False
print(is_prime(161)) # False
print(is_prime(162)) # False
print(is_prime(163)) # True
print(is_prime(164)) # False
print(is_prime(165)) # False
print(is_prime(166)) # False
print(is_prime(167)) # True
print(is_prime(168)) # False
print(is_prime(169)) # False
print(is_prime(170)) # False
print(is_prime(171)) # False
print(is_prime(172)) # False
print(is_prime(173)) # True
print(is_prime(174)) # False
print(is_prime(175)) # False
print(is_prime(176)) # False
print(is_prime(177)) # False
print(is_prime(178)) # False
print(is_prime(179)) # True
print(is_prime(180)) # False
print(is_prime(181)) # True
print(is_prime(182)) # False
print(is_prime(183)) # False
print(is_prime(184)) # False
print(is_prime(185)) # False
print(is_prime(186)) # False
print(is_prime(187)) # False