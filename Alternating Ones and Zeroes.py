def can_alternate(s):
    zeros = s.count('0')
    ones = s.count('1')
    return abs(zeros - ones) <= 1
