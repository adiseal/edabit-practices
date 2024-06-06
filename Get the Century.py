def century(year):
    cent = (year + 99) // 100
    if cent % 10 == 1 and cent != 11:
        suffix = "st"
    elif cent % 10 == 2 and cent != 12:
        suffix = "nd"
    elif cent % 10 == 3 and cent != 13:
        suffix = "rd"
    else:
        suffix = "th"
    return str(cent) + suffix + " century"