def is_identical(s):
    same = all(ch == s[0] for ch in s)
    return same

print(is_identical("aaaax")) 
