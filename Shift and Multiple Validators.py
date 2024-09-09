def is_shifted(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    shift = lst2[0] - lst1[0]
    for i in range(1, len(lst1)):
        if lst2[i] - lst1[i] != shift:
            return False
    return True

def is_multiplied(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    if all(x == 0 for x in lst2):
        return True
    if lst1[0] == 0:
        return False
    multiplier = lst2[0] / lst1[0]
    for i in range(1, len(lst1)):
        if lst1[i] == 0 or lst2[i] / lst1[i] != multiplier:
            return False
    return True

	