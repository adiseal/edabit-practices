def split_code(code):
    alpha_part = ""
    numeric_part = ""
    
    # Iterate over the characters in the code
    for char in code:
        if char.isalpha():
            alpha_part += char
        elif char.isdigit():
            numeric_part += char
    
    # Convert the numeric part to an integer
    numeric_part = int(numeric_part)
    
    return [alpha_part, numeric_part]

