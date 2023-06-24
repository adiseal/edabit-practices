def count_digits(n, d):
    squares = [i**2 for i in range(n + 1)]
    count = 0
    for num in squares:
        count += str(num).count(str(d))
    return count

print(count_digits(10, 1)) # 4