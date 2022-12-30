def mod(a, b):
    # Find quotient (integer part only)
    quotient = int(a / b)
      
    # Find product
    product = quotient * b
    
    # Find modulus (remainder)
    modulus = a - product
    
    return modulus
    
    
    
assert mod(5, 2) == 1

assert mod(218, 5) == 3

assert mod(6, 3) == 0