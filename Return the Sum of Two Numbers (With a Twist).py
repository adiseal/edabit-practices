def sum2(num1, num2):
    # Ensure num1 is the longer string for ease of iteration
    if len(num1) < len(num2):
        num1, num2 = num2, num1
        
    # Reverse the strings to make it easier to add from the right
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    carry = 0
    result = []
    
    # Loop through each digit
    for i in range(len(num1)):
        # Get digit from num1, and if available, from num2; otherwise, use 0
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        
        # Perform the addition with carry
        total = digit1 + digit2 + carry
        result.append(str(total % 10))  # Append the last digit of the total
        carry = total // 10  # Carry the rest to the next column
    
    # If there's a carry left, append it
    if carry:
        result.append(str(carry))
    
    # Reverse to get the correct order and join as a single string
    return ''.join(result[::-1])