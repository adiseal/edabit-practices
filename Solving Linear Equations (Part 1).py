def solve(a, b):
    if a == 1:
        if b == 1:
            return "Any number"
        else:
            return "No solution"
    else:
        # Calculate x using the formula (b - 1) / (a - 1)
        x = (b - 1) / (a - 1)
        return round(x, 3)