def add_odd_to_n(n):
    return sum(range(1, n + 1, 2))


assert add_odd_to_n(5) == 9
# 1 + 3 + 5 = 9

assert add_odd_to_n(13) == 49

assert add_odd_to_n(47) == 576