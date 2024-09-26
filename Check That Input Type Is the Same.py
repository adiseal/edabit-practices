def compare_data(*args):
    # If no input is given or only one input, return True
    if len(args) <= 1:
        return True
    
    # Get the type of the first argument
    first_type = type(args[0])
    
    # Check if all arguments are of the same type
    for arg in args:
        if type(arg) is not first_type:
            return False
    
    return True