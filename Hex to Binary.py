def to_binary(hex_number):
    binary_number = bin(hex_number)[2:]
    return binary_number.zfill(8)