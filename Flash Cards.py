def flash(flashcard):
    num1, operator, num2 = flashcard
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == 'x':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return None
        else:
            return round(num1 / num2, 2)
