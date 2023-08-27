def flatten_the_curve(lst: list) -> list:
    # Check if the list is empty
    if not lst:
        return []
    # Calculate the mean of the numbers in the list
    mean = round(sum(lst) / len(lst), 1)
    # Replace every number with the mean
    result = [mean for _ in lst]
    return result
