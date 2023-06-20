def doubleton(n):
    def is_doubleton(num):
        digits = set(str(num))
        return len(digits) == 2

    n += 1
    while not is_doubleton(n):
        n += 1
    return n
    
print(doubleton(10)) # 12