def operation(num1, num2, op):
    num1 = int(num1)
    num2 = int(num2)

    if op == "add":
        result = num1 + num2
    elif op == "subtract":
        result = num1 - num2
    elif op == "multiply":
        result = num1 * num2
    elif op == "divide":
        if num2 != 0:
            result = num1 // num2
        else:
            return "undefined"
    else:
        return "undefined"

    return str(result)
