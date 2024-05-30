def letter_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    total = abs(len_str1 - len_str2)
    
    for i in range(min(len_str1, len_str2)):
        total += abs(ord(str1[i]) - ord(str2[i]))
        
    return total