def add_nums(nums):
    a = 0
    nums = nums.split(",")
    for x in nums:
        a = a + int(x)
    return a

print(add_nums("2, 5, 1, 8, 4")) # 20