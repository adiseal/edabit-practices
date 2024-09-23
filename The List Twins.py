def twins(lst):
    total_sum = sum(lst)
    left_sum = 0
    
    for i in range(len(lst)):
        left_sum += lst[i]
        if left_sum == total_sum - left_sum:
            return i + 1
    return -1  # Return -1 if no such index is found