def print_all_groups():
    groups = ["a", "b", "c", "d", "e"]
    result = ""
    for year in range(1, 7):
        for group in groups:
            result += str(year) + group + ", "
    return result[:-2]
