def count_all(txt):
    letters = 0
    digits = 0
    for char in txt:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return {"LETTERS": letters, "DIGITS": digits}
