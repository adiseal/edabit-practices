def digit_distance(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    total_distance = 0
    
    for i in range(len(str_num1)):
        digit1 = int(str_num1[i])
        digit2 = int(str_num2[i])
        
        total_distance += abs(digit1 - digit2)
    
    return total_distance