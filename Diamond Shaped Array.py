def diamond_arrays(n):
    result = []
    for i in range(1, n + 1):
        result.append([i] * i)
    for i in range(n - 1, 0, -1):
        result.append([i] * i)
    return result