def upward_trend(lst):
    # Check if there are any strings in the list
    if any(isinstance(x, str) for x in lst):
        return "Strings not permitted!"
    
    # Check if the list is sorted in ascending order
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))


print(upward_trend([1, 2, 3, 4])) # True
print(upward_trend([1, 2, 6, 5, 7, 8])) # False 