def binary_to_decimal(binary):
    binary = ''.join(str(bit) for bit in binary)
    decimal = int(binary, 2)
    return decimal
