def turn_calc(number):
    # Mapping of digits to letters when turned upside down
    digit_to_letter = {
        '0': 'O',
        '1': 'I',
        '2': 'Z',
        '3': 'E',
        '4': 'H',
        '5': 'S',
        '6': 'G',
        '7': 'L',
        '8': 'B',
        '9': '-'
    }
    
    # Convert the number to a string and initialize an empty result
    num_str = str(number)
    result = ""
    
    # Iterate over each digit in the number string
    for digit in num_str:
        if digit in digit_to_letter:  # Check if digit is in our mapping
            result += digit_to_letter[digit]  # Append corresponding letter
            
    # Reverse the result to simulate turning the calculator upside down
    return result[::-1].upper()  # Return uppercase

