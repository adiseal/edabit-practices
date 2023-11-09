def is_narcissistic(n):
    # Convert the number to string to easily get the digits
    str_n = str(n)
    length = len(str_n)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** length for digit in str_n)
    
    # Check if the total is equal to the original number
    return total == n

print(is_narcissistic(8208)) # True
print(is_narcissistic(22)) # False