def add_nums(nums):
    a = 0
    nums = nums.split(",")
    for x in nums:
        a = a + int(x)
    return a

print(add_nums("2, 5, 1, 8, 4")) # 20
print(add_nums("1, 2, 3, 4, 5, 6, 7")) # 28
print(add_nums("10")) # 10