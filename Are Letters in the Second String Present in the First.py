def letter_check(lst):
    str1 = lst[0].lower()
    str2 = lst[1].lower()
    for char in str2:
        if char not in str1:
            return False
    return True

print(letter_check(["trances", "nectar"])) # True
print(letter_check(["compadres", "DRAPES"])) # True