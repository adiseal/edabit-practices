def capital_letters(txt):
    upper = ""
    for i in txt:
        if i.isupper() ==  True:
            upper = upper + i
    return len(upper)
    
print(capital_letters("fvLzpxmgXSDrobbgMVrc"))