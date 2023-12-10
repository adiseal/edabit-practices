def oddish_or_evenish(num):
    num_str = str(num)    
    digit_sum = sum(int(digit) for digit in num_str)    
    if digit_sum % 2 == 0:
        return "Evenish"
    else:
        return "Oddish"
