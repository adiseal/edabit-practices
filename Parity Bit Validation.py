def validate_binary(binary):
    # Count the number of 1s in the binary string excluding the parity bit
    count_ones = binary[:-1].count('1')
    # Check if the count of 1s is even or odd
    if count_ones % 2 == 0:
        # If even, the parity bit should be 0
        return binary[-1] == '0'
    else:
        # If odd, the parity bit should be 1
        return binary[-1] == '1'

print(validate_binary('00101101')) # True
print()validate_binary('11000000') # True