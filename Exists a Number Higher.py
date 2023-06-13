def exists_higher(arr, n):
    if not arr:  # Check if the array is empty
        return False
    
    for num in arr:
        if num >= n:
            return True
    
    return False
    
print(exists_higher([5, 3, 15, 22, 4], 10)) # True