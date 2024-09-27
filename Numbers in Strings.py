def num_in_str(lst):
    # Initialize an empty list to store strings with numbers
    result = []
    
    # Iterate through each string in the provided list
    for string in lst:
        # Check if any character in the string is a digit
        if any(char.isdigit() for char in string):
            result.append(string)
    
    return result