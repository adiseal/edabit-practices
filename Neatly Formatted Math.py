def format_math(expression):
    # Split the expression into parts
    parts = expression.split()
    
    # Perform the calculation based on the operator
    if parts[1] == '+':
        result = int(parts[0]) + int(parts[2])
    elif parts[1] == '-':
        result = int(parts[0]) - int(parts[2])
    elif parts[1] == 'x':
        result = int(parts[0]) * int(parts[2])
    elif parts[1] == '/':
        result = int(parts[0]) // int(parts[2])
    
    # Return the formatted equation
    return "{} = {}".format(expression, result)
