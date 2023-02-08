def sum_digits(n):
    if n == 0:
        return 1
    counter = 0
    n = abs(n)
    while(n):
        counter += 1
        n = int(n/10)
    return counter


print(sum_digits(0)) #➞ 3

#sum_digits(1000) ➞ 4

#sum_digits(1) ➞ 1