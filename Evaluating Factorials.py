import math

def eval_factorial(expressions):
    return sum(math.factorial(int(expr[:-1])) for expr in expressions)
