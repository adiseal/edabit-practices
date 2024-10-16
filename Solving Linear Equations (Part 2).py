def solve(a, b):
    # Check if a - b is zero (i.e., no unique solution)
    if a == b:
        if -3*a + 4 + b == 0:
            return "Any number"
        else:
            return "No solution"
    
    # Solve for x using the simplified formula
    x = (-3*a + 4 + b) / (a - b)
    
    # Return the result rounded to 3 decimal places
    return round(x, 3)