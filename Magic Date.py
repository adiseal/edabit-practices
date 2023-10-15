def magic(date_str):
    # Split the input date string into day, month, and year parts
    parts = date_str.split()
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])

    # Calculate mm * dd
    mm_dd = month * day

    # Calculate the last 1, 2, and 3 digits of yyyy
    last_1_digit = year % 10
    last_2_digits = year % 100
    last_3_digits = year % 1000

    # Check if mm * dd matches the last 1, 2, or 3 digits of yyyy
    return mm_dd in {last_1_digit, last_2_digits, last_3_digits}
    
    
print(magic("1 1 2011")) # True
print(magic("4 1 2001")) # False
print(magic("5 2 2010")) # True
print(magic("9 2 2011")) # False