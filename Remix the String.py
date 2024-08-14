def remix(string, indices):
    # Initialize a list of the same length as the input string with empty strings
    remixed = [''] * len(string)
    
    # Place each character in the string at the corresponding index in the remixed list
    for i, index in enumerate(indices):
        remixed[index] = string[i]
    
    # Join the list into a single string and return it
    return ''.join(remixed)
