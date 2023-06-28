def number_split(num):
    if num % 2 == 0:
        half = num // 2
        return [half, half]
    else:
        half = num // 2
        return [half, half + 1]

print(number_split(4)) # [2, 2]