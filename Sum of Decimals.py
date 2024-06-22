from decimal import Decimal, getcontext

def float_sum(A, B):
    getcontext().prec = 10
    a = Decimal(str(A))
    b = Decimal(str(B))
    return float(a + b)