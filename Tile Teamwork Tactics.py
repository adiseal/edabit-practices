def possible_bonus(a, b):
    return True if b-a < 7 and b-a > 0 else False

print(possible_bonus(3, 7)) # True