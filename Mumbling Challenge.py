def mumbling(s):
    txt = ""
    counter = 1
    for i, x in enumerate(s):
        if i < len(s) - 1:
            txt += "".join(x * counter).capitalize() + "-"
            counter += 1
    return txt + (s[-1] * counter).capitalize()
