def get_decimal_places(n):
    if n.find(".") == -1:
        return 0
    return n[::-1].find(".")




print(get_decimal_places("43"))
