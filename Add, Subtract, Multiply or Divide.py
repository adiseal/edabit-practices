def operation(num1, num2):
    if num1 + num2 == 24:
        return "added"
    elif num1 * num2 == 24:
        return "multiplied"
    elif num1 - num2 == 24:
        return "subtracted"
    elif num1 / num2 == 24:
        return "divided"
    else:
        return None


assert operation(15, 9) == "added"

assert operation(26, 2) == "subtracted"

assert operation(11, 11) == None

print(operation(15, 9)) # "added"
print(operation(26, 2)) # "subtracted"