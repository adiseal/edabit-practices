def median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        median1 = nums[n//2]
        median2 = nums[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = nums[n//2]
    return median

print(median([2, 5, 6, 2, 6, 3, 4])) # 4
print(median([21.4323, 432.54, 432.3, 542.4567])) # 432.4
print(median([-23, -43, -29, -53, -67])) # -43