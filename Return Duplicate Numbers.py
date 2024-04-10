def duplicate_nums(nums):
    num_counts = {}
    duplicates = []

    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    for num, count in num_counts.items():
        if count > 1:
            duplicates.append(num)

    if len(duplicates) == 0:
        return None
    else:
        return sorted(duplicates)

