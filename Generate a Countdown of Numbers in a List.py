def countdown(start):
    start = start + 1
    numbers = range(start)
    count = []
    for x in numbers:
        count.append(x)
    return count[::-1]
    
print(countdown(5)) #➞ [5, 4, 3, 2, 1, 0]