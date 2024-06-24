def solve(equation):
    left_side, right_side = equation.split(' = ')
    
    right_number = int(right_side.strip())
    
    if ' + ' in left_side:
        operator = '+'
    else:
        operator = '-'
    
    parts = left_side.split(' ' + operator + ' ')
    
    if parts[0] == 'x':
        constant = int(parts[1])
    else:
        constant = int(parts[0])
    
    if operator == '+':
        x = right_number - constant
    else:  
        x = right_number + constant
    
    return x