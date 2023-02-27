def longest_string(str1, str2):
    a = str1 + str2
    a = set(a)
    a = sorted(a)
    a = "".join(a)
    return a


str1 = "mubashir"
str2 = "edabit"    
print(longest_string(str1, str2))