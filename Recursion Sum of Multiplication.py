def multi_sum(n, i=1):
    if i == 10:
        return n * i
    else:
        return n * i + multi_sum(n, i + 1)

print(multi_sum(1)) # 55