def worded_math(expression):
    # Dictionary to convert words to numbers
    word_to_num = {
        "zero": 0,
        "one": 1,
        "two": 2
    }
    
    # Dictionary to convert numbers to words
    num_to_word = {
        0: "Zero",
        1: "One",
        2: "Two"
    }
    
    # Split the expression into parts
    parts = expression.lower().split()
    
    # Get the numbers and the operator
    num1 = word_to_num[parts[0]]
    operator = parts[1]
    num2 = word_to_num[parts[2]]
    
    # Perform the operation
    if operator == "plus":
        result = num1 + num2
    elif operator == "minus":
        result = num1 - num2
    else:
        raise ValueError("Unsupported operation")
    
    # Return the result in words with the first letter capitalized
    return num_to_word[result]