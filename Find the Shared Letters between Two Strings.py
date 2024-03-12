def shared_letters(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    common_letters = set(str1) & set(str2)
    result = ''.join(sorted(common_letters))
    return result