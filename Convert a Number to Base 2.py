def binary(decimal):
    if decimal == 0:
        return "0"

    binary_digits = []
    while decimal > 0:
        binary_digits.append(str(decimal % 2))
        decimal //= 2

    binary_digits.reverse()
    return "".join(binary_digits)

print(binary(1)) # "1"