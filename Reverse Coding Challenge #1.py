def mystery_func(txt):
    result = ""
    for i in range(0, len(txt), 2):
        result += txt[i] * int(txt[i+1])
    return result