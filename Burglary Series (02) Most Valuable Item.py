def most_expensive_item(items):
    # Use the max function with the key parameter to find the key with the maximum value
    most_expensive = max(items, key=items.get)
    return most_expensive