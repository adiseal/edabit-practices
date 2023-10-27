def unique_lst(lst):
    seen = set()
    result = []
    for num in lst:
        if num > 0 and num not in seen:
            seen.add(num)
            result.append(num)
    return result


print(unique_lst([-5, 1, -7, -5, -2, 3, 3, -5, -1, -1])) # [1, 3]
print(unique_lst([3, -3, -3, 5, 5, -6, -2, -4, -1, 3])) # [3, 5]