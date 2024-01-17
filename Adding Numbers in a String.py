def add_nums(nums):
    a = 0
    nums = nums.split(",")
    for x in nums:
        a = a + int(x)
    return a

print(add_nums("18, 20, 11, -7, -1, -7, -17, -3, 25, 23, 25, 6, 7, -1, -11, -24, -19, -18, 8, 24, 29, 19, 13, 0, -19, -25, -2, 8")) #➞ 82
print(add_nums("2, 5, 1, 8, 4")) # 20
print(add_nums("1, 2, 3, 4, 5, 6, 7")) # 28
print(add_nums("10")) # 10
print(add_nums("2, 5, 1, 8, 4")) # 20
