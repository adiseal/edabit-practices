def sum_of_cubes(nums):
    sums = []
    for x in nums:
        sums.append(x ** 3)
    return sum(sums)
    
print(sum_of_cubes([3, 4, 5]))