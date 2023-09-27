def complete_binary(bin_str):
    # Calculate the number of zeros to add
    zeros_to_add = len(bin_str) % 8
    if zeros_to_add != 0:
        zeros_to_add = 8 - zeros_to_add

    # Add the necessary zeros to the start of the string
    return '0' * zeros_to_add + bin_str
