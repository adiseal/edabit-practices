def stupid_addition(a, b):
    if type(a) == type(b):
        if isinstance(a, str):
            return int(a) + int(b)
        elif isinstance(a, int):
            return str(a) + str(b)
    else:
        return None
