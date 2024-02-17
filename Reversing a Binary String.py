def reversed_binary_integer(n):
    binary = bin(n)[2:]  
    reversed_binary = binary[::-1]  
    return int(reversed_binary, 2)  