def join_digits(n):
    result = []
    for i in range(1, n + 1):
        result.extend(str(i))
    return '-'.join(result)

