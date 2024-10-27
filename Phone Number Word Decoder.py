def text_to_num(phone_number):
    # Mapping of letters to corresponding digits
    letter_to_digit = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    # Convert each character in the phone number
    converted_number = []
    for char in phone_number:
        if char.isalpha():  # Check if the character is a letter
            converted_number.append(letter_to_digit[char])
        else:
            converted_number.append(char)  # Keep numbers and symbols as they are

    # Join the list into a single string and return
    return ''.join(converted_number)