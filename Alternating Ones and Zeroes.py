def can_alternate(s):
    zeros = s.count('0')
    ones = s.count('1')
    return abs(zeros - ones) <= 1

print(can_alternate("0001111")) # True
print(can_alternate("01001")) # True
print(can_alternate("010001")) # False
print(can_alternate("0100110111")) # False
print(can_alternate("10101010")) # True
print(can_alternate("010101000")) # False
print(can_alternate("0111")) # False
print(can_alternate("00")) # False
print(can_alternate("1111")) # False
print(can_alternate("101")) # True