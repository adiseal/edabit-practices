def integral(b, m, n):
    def f(x):
        return (b + 1) * x ** b
    def F(x):
        return x ** (b + 1)
    return F(n) - F(m)