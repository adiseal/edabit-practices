def string_cycling(str1, str2):
    cycles = len(str2) // len(str1) + 1
    repeated_str1 = (str1 * cycles)[:len(str2)]
    return repeated_str1
    
print(string_cycling("abc", "hello")) # "abcab"