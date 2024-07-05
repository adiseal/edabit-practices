def smallest(N, value):
    # Calculate the smallest N-digit number
    smallest_number = 10 ** (N - 1)
    
    # Find the smallest multiple of 'value' greater than or equal to 'smallest_number'
    while smallest_number % value != 0:
        smallest_number += 1
    
    return smallest_number