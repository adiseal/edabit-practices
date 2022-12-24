def add_binary(a, b):
    sum = bin(a + b)
    return sum[2:]



assert add_binary(1, 1) == "10"

assert add_binary(1, 2) == "11"

assert add_binary(4, 5) == "1001"