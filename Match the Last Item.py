def match_last_item(lst):
    concatenated = ''.join(map(str, lst[:-1]))
    return concatenated == str(lst[-1])