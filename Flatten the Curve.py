def flatten_the_curve(lst: list) -> list:
    # Check if the list is empty
    if not lst:
        return []
    # Calculate the mean of the numbers in the list
    mean = round(sum(lst) / len(lst), 1)
    # Replace every number with the mean
    result = [mean for _ in lst]
    return result

print(flatten_the_curve([1, 2, 3, 4, 5])) # [3, 3, 3, 3, 3]
print(flatten_the_curve([0, 0, 0, 2, 7, 3])) # [2, 2, 2, 2, 2, 2]
print(flatten_the_curve([4])) # [4]
print(flatten_the_curve([])) # []