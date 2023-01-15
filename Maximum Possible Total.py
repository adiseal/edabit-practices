def max_total(nums):
    nums.sort()
    return sum(nums[5:])
    
    
assert max_total([1, 1, 0, 1, 3, 10, 10, 10, 10, 1]) == 43

assert max_total([0, 0, 0, 0, 0, 0, 0, 0, 0, 100]) == 100

assert max_total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 40