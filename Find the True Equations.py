def true_equations(equations):
    true_eqs = []
    for eq in equations:
        left, right = eq.split('=')
        if eval(left) == eval(right):
            true_eqs.append(eq)
    return true_eqs