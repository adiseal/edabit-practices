def str_match_by2char(a, b):
    # Initialize the count to 0
    count = 0

    # Get the minimum length of the two strings
    min_len = min(len(a), len(b))

    # Iterate over the range of the minimum length minus 1
    for i in range(min_len - 1):
        # If the two characters in both strings are the same
        if a[i:i+2] == b[i:i+2]:
            # Increment the count
            count += 1

    # Return the count
    return count
