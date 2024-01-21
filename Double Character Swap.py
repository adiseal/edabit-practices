def double_swap(txt, c1, c2):
    return "".join([c2 if i == c1 else c1 if i == c2 else i for i in txt])