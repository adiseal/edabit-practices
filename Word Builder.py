def word_builder(letters, positions):
    # Create an empty list with the same length as letters
    result = [''] * len(letters)
    
    # Place each letter in its corresponding position
    for letter, position in zip(letters, positions):
        result[position] = letter
    
    # Join the list into a string and return it
    return ''.join(result)