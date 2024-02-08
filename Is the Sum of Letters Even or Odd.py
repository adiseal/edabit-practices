def is_alpha(s):
    s = s.lower()  
    total = sum(ord(c) - 96 for c in s if c.isalpha())  
    return total % 2 == 0  