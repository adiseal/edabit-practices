def print_all_groups():
    groups = ["a", "b", "c", "d", "e"]
    result = ""
    for year in range(1, 7):
        for group in groups:
            result += str(year) + group + ", "
    return result[:-2]
    
print(print_all_groups()) # "1a, 1b, 1c, 1d, 1e, 2a, 2b, 2c, 2d, 2e, 3a, 3b, 3c, 3d, 3e, 4a, 4b, 4c, 4d, 4e, 5a, 5b, 5c, 5d, 5e, 6a, 6b, 6c, 6d, 6e "
