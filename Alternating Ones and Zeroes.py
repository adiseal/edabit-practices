def can_alternate(s):
    zeros = s.count('0')
    ones = s.count('1')
    return abs(zeros - ones) <= 1

print(can_alternate("0001111")) # True
print(can_alternate("01001")) # True
print(can_alternate("010001")) # False
print(can_alternate("0100110111")) # False