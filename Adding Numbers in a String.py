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