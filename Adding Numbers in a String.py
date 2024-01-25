def add_nums(nums):
    a = 0
    nums = nums.split(",")
    for x in nums:
        a = a + int(x)
    return a

print(add_nums("2, 5, 1, 8, 4")) # 20
print(add_nums("1, 2, 3, 4, 5, 6, 7")) # 28
print(add_nums("10")) # 10
print(add_nums("-12, -8, 2, 11, -16, 16")) # -7
print(add_nums("25, -4, -15, -7, 27, 12, 29, -6, 20, 9")) # 90
print(add_nums("24, 7, -15, -28, -21, 6, 5, -6, 23, 24, -22, 30, -21, -10, -10, -12, 24, -18, -13, -27, 22, -30, -11, -13, 6, 7, 27, 1")) # -51
print(add_nums("-17, -18, -18, -14, -8, 0, 12, 2, 10, 5, -8, 12, -17, 8, -5, -23, 2, 29, -30, 13, -22, 19, 13, -18, -8")) # -81
print(add_nums("16, 8, 19, 25, 18, 26, 2, 14")) # 128
print(add_nums("-18, -10, 9, 12, -16, 22, 2, 17, 10, -25, 1, -25, -15, -29, 12, 11, 4")) # -38
print(add_nums("12, -30, 26, -18, -4, 25, 19, -22, 7, -17, 3, -30, -27, 10, -12, -12, -24")) # -94
print(add_nums("0, 21, 20, 0, 26, -9, 12, -9, 20")) # 81
print(add_nums("-27, 28, -9, -9, 4, -22, -13, 0, -2, 19, 9, 5, 20, 21, -3, 22, 6, -10, -1, -12, 2")) # 28
print(add_nums("13, -29, 13, 22, 23, 14, 2")) # 58
print(add_nums("-18, 3, 30, 13, 20, -23, -18, -27, -30, 1, -19, -3, -19, -22, -1")) # -113
print(add_nums("18, 20, 11, -7, -1, -7, -17, -3, 25, 23, 25, 6, 7, -1, -11, -24, -19, -18, 8, 24, 29, 19, 13, 0, -19, -25, -2, 8")) # 82
print(add_nums("-13, -30, -1, -9, -25, -9, 11, -28, 0, 10, -23, -20, -5, 21, -29, 6, 20, -23, -23, -24, 30, -14, 24")) # -154
print(add_nums("5, -16")) # -11