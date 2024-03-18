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
print(median([20, 40, 20, 30, 50, 60, 70, 0, 20])) # 30
print(median([342, 98, 5456, 32, 786, 432, 890, 321])) # 387
print(median([1, 0, 1, 0, 0, 0, 1, 1])) # 0.5
print(median([32, 5, 78, 32, 4, 5, 3])) # 5
print(median([-20, 40, 30, -2, 40, -13])) # 14
print(median([32786, 7837, 83736, 83736, 10383, 738393])) # 58261
print(median([7685, 83736, 38376, 73638, 7337])) # 38376
print(median([0, 0, 0, 0])) # 0