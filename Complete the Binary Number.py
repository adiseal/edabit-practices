def complete_binary(bin_str):
    # Calculate the number of zeros to add
    zeros_to_add = len(bin_str) % 8
    if zeros_to_add != 0:
        zeros_to_add = 8 - zeros_to_add

    # Add the necessary zeros to the start of the string
    return '0' * zeros_to_add + bin_str

print(complete_binary("1100")) # "00001100"
print(complete_binary("1101100")) # "01101100"
print(complete_binary("110010100010")) # "0000110010100010"