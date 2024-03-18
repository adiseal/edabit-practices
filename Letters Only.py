def letters_only(s):
    if s == "":
        return False
    for char in s:
        if not char.islower() and not char.isspace():
            return False
    return True