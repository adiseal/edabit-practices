def normalize(txt):
    if txt == txt.upper():
        return txt.capitalize() + "!"
    else:
        return txt
        
print(normalize("Today is not caps lock day.")) # "Today is not caps lock day."