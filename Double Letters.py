def double_letters(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

print(double_letters("loop")) # True
print(double_letters("yummy")) # True
print(double_letters("orange")) # False
print(double_letters("munchkin")) # False