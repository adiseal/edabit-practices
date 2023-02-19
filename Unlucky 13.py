def unlucky_13(nums):
    lst = []
    for x in nums:
        if x % 13 != 0:
            lst.append(x)
    return lst


print(unlucky_13([53, 182, 435, 591, 637])) #➞ [53, 435, 591]