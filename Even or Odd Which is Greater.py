def even_or_odd(s):
    even_sum = 0
    odd_sum = 0
    for char in s:
        if char.isdigit():
            if int(char) % 2 == 0:
                even_sum += int(char)
            else:
                odd_sum += int(char)
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
        
print(even_or_odd("22471")) # "Even and Odd are the same"
print(even_or_odd("213613")) # "Even and Odd are the same"

